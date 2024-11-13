These are independent one-off tools. Maybe you'll find one or more
of them helpful.

### [gpr](gpr) - git pr checkout

Sweet front end to `git pr` (in the `git-extras` rpm). Best feature
is that it handles iterative PR pulls, and shows you easy instructions
for reviewing diffs between two iterations of a PR. See its `--help`.

### [install-podman](install-podman) - simple VM setup for building podman

One-stop helper for setting up podman sources on a 1mt VM.
Installs prerequisites, does a git checkout into `/root/go/podman`.
```
$ ./install-podman 10.0.123.456
```

### [jira](jira) - command-line access to Jira

Wrapper for command-line jira (containerized tool). All I ever use it
for is `jira mine`, which shows a navigable screen with my Jiras. Only
useful for those of us who prefer terminal over browser.

### [stale-issues](stale-issues) - generate table of stale Podman issues

Used for RUN-1722, a thorny issue I've never been able to resolve (automatic
closing of stale issues).

This script offers a little help for a manual approach: it generates a
Markdown table, suitable for pasting into Jira, showing the number of
bugs/features/other that have been stale past a number of days. More
importantly, each of those numbers is a _link_ to you can click on
each one, view the list, and decide which ones you want to close.

The code is horrible, a cobbled-together hack that I never cleaned up.

Usage:
```
$ ./stale-issues | xsel -b -i    (then paste into Jira)
```
or
```
$ ./stale-issues github | xsel -b -i   (and paste into Github)
```
