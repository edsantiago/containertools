Scripts for tracking Cirrus credits and warning
when they run low.

The script that does all the work is [cirrus-credits](cirrus-credits).
Much to your likely astonishment, this is a trivial simple script.
The bulk of the work is done in a single one-liner. The rest is
deciding whether to log to a CSV history file (when run from cron)
or not, and whether or not to send warning email to Ed.

I run it daily from cron. Running it at the same time is necessary
for tracking daily usage.
```
5  5         * * *     /home/esm/bin/scripts/cirrus-credits
```

The other script is [cirrus-credits-usage](cirrus-credits-usage).
This one gives you a multi-line listing, day by day, usage each day.
It is intended to run interactively, then possibly copypasted to
send email to the team for their awareness.

Example:
```
$ cirrus-credits-usage
....
Sun Oct 27 05:05:01   0.2
Mon Oct 28 05:05:01   0.3
Tue Oct 29 05:05:00   1.9
Wed Oct 30 05:05:00   1.5
Thu Oct 31 05:05:01   0.8
Fri Nov 01 05:05:00   1.2
Sat Nov 02 05:05:00   0.0
Sun Nov 03 05:05:01   0.0
Mon Nov 04 05:05:00   0.0
Tue Nov 05 05:05:01   0.0
Wed Nov 06 05:05:01   0.0
Thu Nov 07 05:05:00   0.0  balance: 103.24; @ 0.39/day will run out ~07/29
```
