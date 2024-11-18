This directory contains files you can use to monitor OpenQA.

Setup
=====

```
# dnf install fedora-messaging
```
For each of the files below, search for REPLACEME and replace
as appropriate, then copy:

```
  podman.py
  podman.toml   - put these in ~/.config/fedora-messaging/
  ^^^^^^^^^^^<--- edited version of /etc/fedora-messaging/fedora.toml

  podman-openqa.service - put in ~/.config/systemd/user
```

Then:

```
$ systemctl --user daemon-reload
$ systemctl --user start podman-openqa.service
```

You will get email any time a message comes in where test_type
contains "podman" and result is not "passed". Email will
contain a link at the top, click on that to see openqa results.

(Note: sometimes the failure is in `_advisory_update`. You can
probably ignore those, they usually indicate an infrastructure
problem or a problem with the package itself. Errors in `podman`,
you need to look at. As of 2024-11-18 the fedmsg structure does
not include an indication of where the failure occurred. Adam
Williamson is aware of this gap, his response on 2024-08-29 is:

>Subject: Re: Request: OpenQA message bus: new field, where did it fail?
>
>Hey, Ed. It should be possible, I'm not sure how much work it'll be - I
>may need to do something upstream. It'd more likely be added to the
>openqa.job.done message than the ci.fedora-update.test.complete message
>- the format of CI messages is standardized in
>https://pagure.io/fedora-ci/messages , it's easier for me to tweak the
>openqa-specific messages. The openqa.* messages are more or less direct
>conversions of events in openQA's internal event system, the CI
>messages are transformed from those. I'll try and look into it when I
>get a minute.


).

Monitoring
==========

You can check that it's working by looking in /var/tmp/fedmsg-podman
or whatever you set "path" to. Messages come in every few minutes.

Useful links
============

Or, they were useful to me at the time I set all this up a year ago. YMMV.

   https://github.com/containers/podman/issues/19299
   https://github.com/containers/podman/pull/19302

   https://pagure.io/fedora-ci/messages

   https://fedora-messaging.readthedocs.io/en/stable/user-guide/configuration.html#consumer-options

   https://fedora-messaging.readthedocs.io/en/stable/user-guide/consuming.html

   https://apps.stg.fedoraproject.org/datagrepper/v2/id?id=bfd596b3-0aa2-4e30-ab02-8b118a5ce9fa&is_raw=true&size=extra-large

   https://fedora-messaging.readthedocs.io/en/stable/user-guide/schemas.html
