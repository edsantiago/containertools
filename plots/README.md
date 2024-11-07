Scripts for producing time-series plots of Cirrus CI timings on PRs.
(see
[podman](https://www.edsantiago.com/cirrus-timing-history/podman.html),
[buildah](https://www.edsantiago.com/cirrus-timing-history/podman.html),
[skopeo](https://www.edsantiago.com/cirrus-timing-history/podman.html)).


[doit](doit) is the principal wrapper. I invoke it as:
```
$ ~/src/redhat/cirrus-timing-history/doit
```
In that directory I have three checked-out directories: `buildah`,
`podman`, `skopeo`. I do not work in these directories or do
anything whatsoever in them. They're really just a waste of space,
but I need them in order to do `git pull` then `git log`, and
get PR numbers and commit times from that log.

[cirrus-timing-history](cirrus-timing-history) is the script
that generates the plots. It relies on [cirrus-pr-timing](../ci-watch/cirrus-pr-timing).
