This is the script that creates package-version-distro tables
on automation_images PRs, e.g., [PR 390](https://github.com/containers/automation_images/pull/390#issuecomment-2455536491) (Bump to F41, plain table) and [PR 391](https://github.com/containers/automation_images/pull/391#issuecomment-2455073982) (comparison against previous build, shows only diffs).

Unfortunately this was written to use MH-style email message files.
Making this work with other MUAs is left as an exercise for the reader.

Workflow
========

1. automation_images PR
1. when successful, sends email from `github-actions[bot]` with a table
of base and cache image names, each of them including a link to a
Cirrus task.
1. You (manually) pipe this email to `cirrus-vm-get-versions`, then
(manually) paste output into the PR.

Examples
========

**Usual case**: just a regular bump to get up-to-date packages
in the same VM setup. This will give you a table showing only
which packages changed between two VM build PRs:

```
$ cirrus-vm-get-versions --skip --baseline=c20241104t170243z-f41f40d13 ~/Mail/myfolder/2345 |xsel -b -i
```

**Distro Change**: When doing a major bump PR, like f40 to f41 or otherwise
changing the set of VMs, a diff is pointless. This gives you a full table
of all packages and their versions:
```
$ cirrus-vm-get-versions ~/Mail/myfolder/1234 |xsel -b -i
```

Files
=====

Script fetches build logs and stores them under `~/.cache/cirrus-vm-get-versions/<IMG_SFX>`
