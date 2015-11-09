# GitHubTimeTracker
[![Build Status](https://travis-ci.org/rdev-hackaton/GitHubTimeTracker.svg?branch=master)](https://travis-ci.org/rdev-hackaton/GitHubTimeTracker)
[![Coverage Status](https://coveralls.io/repos/rdev-hackaton/GitHubTimeTracker/badge.svg?branch=master&service=github)](https://coveralls.io/github/rdev-hackaton/GitHubTimeTracker?branch=master)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/rdev-hackaton/GitHubTimeTracker?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

GitHubTimeTracker is a python library inspired on [StephenOTT](https://github.com/StephenOTT) / [Github-Time-Tracking](https://github.com/StephenOTT/GitHub-Time-Tracking)
for tracking time and budget spent on a project.

## Installation
    pip install git+https://github.com/rdev-hackaton/GitHubTimeTracker

## Usage

### CLI
GitHubTimeTracker comes with a simple command-line interface. Just type `ghtt` to enter interactive mode, or toss in a few options to filter the results.

```
Usage: ghtt [OPTIONS]

  Print time/budget info

Options:
  --token TEXT           Your GitHub personal access token.
  --login TEXT           Your GitHub login (use this or token, not both).
  --password TEXT        Your GitHub password.
  --repo TEXT            Repository.
  --committer TEXT       Limit results to given committer.
  --issue INTEGER        Limit results to commits related to given issue.
  --milestone TEXT       Limit results to commits related to given milestone.
  --total / --non-total  Give total time/budget instead of a list of entries.
  --help                 Show this message and exit.
```

### Time logging
Activities should be prefixed with an amount of time spent on them. The prefix has a few variations:

| Example | Code |
| --------- | ------ |
| :clock1: 15m \| Initial research | `:clock1: 15m | Initial research` |
| :clock12: 2h 30m \| Fix the javascript error on safari | `:clock12: 2h 30m | Fix the javascript error on safari` |
| :clock5: 4d16h Yak shaving | `:clock5: 4d16h Yak shaving` |

The line should begin with a clock emoji, and then be followed by `d`, `h` or `m` for days, hours and minutes. Any text after that will be treated as a comment to the time log entry.

You can use this syntax to log time spent on commits, issues, pull requests and so forth.

## Authors
[<img alt="Marek Bednarski" src="https://avatars2.githubusercontent.com/u/13423250" height="60px">](https://github.com/b-me)
[<img alt="Filip Figiel" src="https://avatars1.githubusercontent.com/u/4096683" height="60px">](https://github.com/megapctr)
[<img alt="Łukasz Haze" src="https://avatars1.githubusercontent.com/u/2180285" height="60px">](https://github.com/lhaze)
[<img alt="Łukasz Kożuchowski" src="https://avatars3.githubusercontent.com/u/1458848" height="60px">](https://github.com/evalapply)
[<img alt="Piotr Pęczek" src="https://avatars0.githubusercontent.com/u/2931838" height="60px">](https://github.com/ppeczek)
[<img alt="Jakub Skałecki" src="https://avatars3.githubusercontent.com/u/3935986" height="60px">](https://github.com/Valian)
