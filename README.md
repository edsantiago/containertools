This repo contains scripts that Ed uses regularly, and brief
descriptions of how/when/why they're used.

* [cirrus-credits](cirrus-credits/) - track Cirrus credits, warn if low
* [cirrus-cronjobs](cirrus-cronjobs/) - simplified maintenance of nightly CI runs
* [cirrus-vm-get-versions](cirrus-vm-get-versions/) - generate table of package
versions on `automation_images` (new-VM) PRs
* [ci-watch](ci-watch/) - console tool for monitoring running CI jobs
* [flakes](flakes/) - the big one. Tools for tracking and cataloging flakes.
* [get-cirrus-buildid-for-pr](get-cirrus-buildid-for-pr) - one of the most useful
scripts I have. Feed it a PR, it will (if possible) spit out the Cirrus BuildID
for that PR. (Remember, a Cirrus *build* is a set of many *tasks*, each of which
is a VM-test combination)
* [openqa-listener](openqa-listener) - alert if podman openqa jobs fail
* [orphan-kill](orphan-kill/) - helper for handling "orphan VM" emails
* [plots](plots/) - generate time-series plots showing how long CI jobs take
