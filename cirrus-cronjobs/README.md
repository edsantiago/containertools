Scripts for maintaining the list of Cirrus cron jobs.

[cirrus-get-cronjobs](cirrus-get-cronjobs)
=====================

This is the main script. It operates on the file
`~/doc/rclone/Containers/Cirrus-Cron Calculator.xlsx`
which you will need to find and track on your own.
I highly recommend [rclone](https://rclone.org/drive/).

```
$ rclone sync -v rh: ~/doc/rclone/                               - (42)
<6>INFO  : There was nothing to transfer
<6>INFO  :
```

Usage:
```
$ ./cirrus-get-cronjobs
cirrus-get-cronjobs: podman v4.9: EOL date 2024-11-12 is coming up!
aardvark-dns  https://cirrus-ci.com/settings/repository/6483741884284928
   main                 0  0  5 ? * 1-5
   v1.0.1-rhel          0  0  4 ? * 1
   v1.1.0-rhel          0  0  3 ? * 2
   v1.12                0  0  2 ? * 3
....
```
The lines above show agreement between the spreadsheet and Cirrus.
If any were to disagree, there would be big warning signs.

If you encounter discrepancies, click the cirrus link, delete the
existing job (if any), then create a new job by copy-pasting the
branch into two input boxes and the cron string into the right-hand
one. You have to delete and recreate because Cirrus has no way
to edit.

[cirrus-get-cronjobs-nightly](cirrus-get-cronjobs-nightly)

For simplicity, I run this script in my nightly cron:
```
1  4         * * *    cirrus-get-cronjobs-nightly
```
It is silent unless something changes. When something changes,
I then run `cirrus-get-cronjobs` manually. See above.

I don't run `rclone` in cron, so this cron job is really
pointless except to warn me about upcoming EOLs.
