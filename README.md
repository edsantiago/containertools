This repo contains scripts that Ed uses regularly, and brief
descriptions of how/when/why they're used.

Ad Hoc
======

Scripts I run when needed:

* [ci-watch](ci-watch/) - console tool for monitoring running CI jobs. I run
it pretty much on every PR I submit and resubmit.
* [cirrus-vm-get-versions](cirrus-vm-get-versions/) - generate table of package
versions on `automation_images` (new-VM) PRs. I run it every time I get
that little table email showing VM 'cYYYYMMDD' numbers.
* [get-cirrus-buildid-for-pr](get-cirrus-buildid-for-pr) - one of the most useful
scripts I have. Feed it a PR, it will (if possible) spit out the Cirrus BuildID
for that PR. (Remember, a Cirrus *build* is a set of many *tasks*, each of which
is a VM-test combination). I don't actually run it manually, but many of the
scripts in this tree call it.
* [git-sha-to-pr](git-sha-to-pr/) - given a git SHA, shows its corresponding PR.
* [orphan-kill](orphan-kill/) - helper for handling "orphan VM" emails. I
run it once a week or so, when I get one of those orphan emails.

At Least Daily, Manually
========================

* [flakes](flakes/) - the big one. Tools for tracking and cataloging flakes.
* [plots](plots/) - generate time-series plots showing how long CI jobs take.
This one should run from cron, maybe every 2-4 hours. It's just too new so I
wanted to get a sense for it (results, unexpected hiccups) before letting go.

Cron
====

Mostly run from cron, with occasional human intervention when I see unexpected
results in my morning email:

* [cirrus-credits](cirrus-credits/) - track Cirrus credits, warn if low
* [cirrus-cronjobs](cirrus-cronjobs/) - simplified maintenance of nightly CI runs
* [quay-check](quay-check) - make sure quay.io images have reasonable descriptions

This one is quadlet, not cron, but same idea, it runs unattended:

* [openqa-listener](openqa-listener) - alert if podman openqa jobs fail.
