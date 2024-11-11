Every week or two we get "Orphaned CI VMs detected" emails:

```
Date: Fri, 08 Nov 2024 00:02:01 +0000 (UTC)
From: Do Not Reply <nobody@podman.io>
To: rh.container.bot@gmail.com, podman-monitor@lists.podman.io
Subject: [Podman-monitor] Orphaned CI VMs detected

Detected 1 Orphan VM(s):

Orphaned libpod-218412 VMs:
* VM packer-67290d3f-b7b3-e470-1c67-33f7409c968a running 3 days with labels 'rel
ease=fedora-41;sfx=20241104t170243z-f41f40d13;src=build-push-b20241104t170243z-f
41f40d13;stage=cache'

# Source: check_orphan_vms workflow on containers/automation_images.
```

Normal human beings can't deal with that. Is that a Google VM or Amazon?
What the heck do you do with that? Where do you go, how do you kill it?

Pipe your email to [orphan-kill](orphan-kill) and maybe it'll help. It'll
try to open a browser page to the right place. From there you can `stop`
and `delete` the VMs.

Unfortunately, it's imperfect. On October 22 I ran it, and it just 404ed.
The reason turned out to be that the bad VMs had a different zone name
than what the script has hardcoded. (It has to hardcode, because the
zone name is not included in the email). If you get a 404, try changing
the zone name in the script.

Also, some VMs have an attached disk, and you need to delete those _after_
deleting the VM. Left as an exercise for the reader.

A better solution might be to fix the email script itself so it
includes links to the right places. Good luck.
