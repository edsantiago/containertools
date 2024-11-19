This is an overview of Ed's flake-catalog process.

It is unlikely that you will be able to use any of these tools without
heavy surgery, if at all. I'm sorry. A sufficiently motivated person
may be able to recreate better, more maintainable versions of these
tools by perusing the GraphQL queries and skimming the logic flow.

Workflow
========

I run `cirrus-flake-catchup` several times a day. Once in a while, when I
see flakes in a PR that is not likely to merge as-is, I also manually run
```
$ cirrus-flake-summarize PR-NUMBER
```
After running either of these, I look at the flake logs and run a
series of `cirrus-flake-assign` commands, followed again by
`cirrus-flake-catchup` so it regenerates the html.

Setup
=====
```
# dnf install perl-open perl-DBI perl-DBD-SQLite perl-JSON perl-libwww-perl \
              perl-Data-TreeDumper perl-Time-Piece perl-LWP-Protocol-https \
              sqlite3
```

Details
=======

[cirrus-flake-catchup](cirrus-flake-catchup)
--------------------

This is a simple shell script. For each project (podman buildah etc),
it queries github for recently closed PRs, and runs `cirrus-flake-summarize`
on each one that we haven't already seen. Once done, runs `cirrus-flake-xref`
which is what generates the HTML pages.

[cirrus-flake-summarize](cirrus-flake-summarize)
----------------------

By far the most complicated script here. Given a PR or a task ID,
downloads the logs and looks for e2e and system test failures.
Every one it finds gets saved into a local DB with the VM type,
test name, error message string, and a unique ID number. This
ID number is used by `cirrus-flake-assign` to sort into buckets.

You will rarely need to invoke this directly, because it is invoked
by `cirrus-flake-catchup`, but you need to know how to read its output:
```
$ cirrus-flake-summarize --project=buildah 5552
#### Containerized Integration

  2024-11-07T10:00:20  [integration_test](https://api.cirrus-ci.com/v1/task/5891834289848320/logs/integration_test.log)
cirrus-flake-summarize: Warning: No annotated log: https://api.cirrus-ci.com/v1/artifact/task/5891834289848320/html/Containerized-Integration.log.html
*   [Containerized] bud: build push with --force-compression
3224
```
First line is the test name. Next few lines are links to logs. Final line
is a flake ID (in my flake database) suitable for `cirrus-flake-assign`.

WHEN TO RUN IT MANUALLY

You're watching a PR; maybe yours, maybe someone else's. PR is still
in review. You notice a test failure, and realize it's a flake. No
other tests fail, or maybe 1-2 other flakes. No real test failures.
But you don't know if the PR is going to be approved and merged, or
re-pushed for other reasons. If the PR is re-pushed, you lose this
flake history, and that matters because this particular flake
instance (root/rootless, local/remote, fedora 48/49) might
possibly add useful data to the flake catalog.

In this case, run `cirrus-flake-summarize PR-NUMBER`. Even if the
PR isn't merged. Even if you haven't re-run the flakes. This adds
the flake to the catalog, and you can review it later. (There is
no danger of dups. Flakes are keyed by Cirrus TaskID, which is
unique).

[cirrus-flake-xref](cirrus-flake-xref)
-----------------

Generates HTML pages organized by flake.

As a bonus, this script can also generate Github markdown suitable
for posting in an issue. This is useful when filing or updating
issues, because it generates a summary with links, test names,
and a checklist of which test-machine combinations have experienced
this flake:
```
$ cirrus-flake-xref --markdown --since=90 --filter=19048 | xsel -b -i
```

[cirrus-flake-assign](cirrus-flake-assign)
-------------------

This is how you assign individual failures into buckets, i.e.,
"oh, I'm seeing this error message, that means Issue #12345."
Because humans are better at remembering strings than numbers,
the script accepts keywords from an Issue title:
```
$ cirrus-flake-assign "toctou bind address use" 37790
*** -> #19048 run -P: TOCTOU in port allocation: bind: address already in use

Podman kube play test with reserved PublishAll annotation in yaml
  int remote debian-13 root host sqlite
    PR 24412 @ 11-05 07:35
    - Ok? y
```

Important special case: IDs `9999x` are reserved for "not yet filed".
Sometimes I see a few instances of flakes that look related but
they manifest in different tests, hence they don't get clustered
in the HTML page. For those I will usually do:
```
$ cirrus-flake-assign 99999 12345 12346 12347 12348
$ cirrus-flake-catchup
```
(or 99998, or 7, when I've got more than one in flight).

This will force-cluster them in one HTML group, from which I
can look for patterns. If they merit filing an issue, and
they usually do, I use `cirrus-flake-xref --markdown --filter=99999`
and include the output when filing the issue.

Once you've filed the issue, update the DB:
```
$ sqlite3 ~/.local/share/cirrus-flake-summarize/podman/db.sqlite
SQLite version 3.45.1 2024-01-30 16:01:20
Enter ".help" for usage hints.
sqlite> UPDATE flakes SET flake='24571' WHERE flake='99999';
```

[cirrus-flake-grep](cirrus-flake-grep)
-----------------

Only used ad hoc, when I notice a new flake pattern and want
to see if it's really new or if we've seen it before.
```
$ cirrus-flake-grep 'failed to move mount'
Podman checkpoint - [It] podman checkpoint container with export and try to change the runtime - 6726977221033984
* int podman rawhide root host sqlite
  * PR #17831 [08-11 07:26]
   [+0943s]   9c8758400f11
   ...log excerpt
```
My current flake db is 4.1G; this can take O(1 minute). The database
files are much too huge to commit into this repo, sorry.
