Usage
=====

```bash
$ ci-watch 17831
```

This will run forever, clearing screen and displaying timing:
```
17831 CI: keep hammering on sqlite, without flake retries
| type | user     | Rc |      d13 |      f39 |      f40 |   f40-aa |      raw |
| ---- | -------- | -- | -------- | -------- | -------- | -------- | -------- |
| int  | root     |    |    15:03 |    16:57 |    17:30 |    10:58 |    16:38 |
| int  | root     | R  |    14:21 |    16:37 |    16:54 |          |    17:34 |
| int  | root     |  c |          |    15:38 |    15:05 |          |          |
| int  | rootless |    |    14:33 |    15:17 |    16:37 |          |    14:46 |
| sys  | root     |    |    27:29 |    28:22 |    25:19 |    21:33 |    26:40 |
| sys  | root     | R  |    21:23 |    18:44 |    18:02 |    14:20 |    18:36 |
| sys  | rootless |    |    29:21 |    28:52 |    26:04 |          |    25:50 |
| sys  | rootless | R  |          |          |    16:23 |          |          |
| mach | rootless |    |          |          |    18:18 |          |          |
```

If you have multiple PRs in flight, feed it all the PR numbers.

`ci-watch` calls `cirrus-pr-timing`. You may find it useful to call
that script too.

NOTE
====
You will need a `$GITHUB_TOKEN`. Getting that and setting it
(securely) in your environment is left as an exercise for the reader.


-------------------------

```bash
$ cirrus-get-cronjobs
...
podman  https://cirrus-ci.com/settings/repository/6707778565701632
   v3.0.1-rhel          20 20 20 ? * 1-6     [ EXPECTED: 0 30 2 ? * 2 * ]
   v1.6.4-rhel          19 19 19 ? * 1-6     [ EXPECTED: 0 0 4 ? * 1 * ]
   v5.2                 18 18 18 ? * 1-6     [ EXPECTED: 0 0 13 ? * 3 * ]
   main                 17 17 17 ? * 1-6     [ EXPECTED: 0 30 4 ? * 1-5 * ]
   .....
```
Finding the spreadsheet is left as an exercise for the reader.
