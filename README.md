# GitHubTimeTracker

[![Build Status](https://travis-ci.org/rdev-hackaton/GitHubTimeTracker.svg?branch=master)](https://travis-ci.org/rdev-hackaton/GitHubTimeTracker)
[![Coverage Status](https://coveralls.io/repos/rdev-hackaton/GitHubTimeTracker/badge.svg?branch=master&service=github)](https://coveralls.io/github/rdev-hackaton/GitHubTimeTracker?branch=master)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/rdev-hackaton/GitHubTimeTracker?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

GitHubTimeTracker is a python library inspired on [StephenOTT](https://github.com/StephenOTT) / [Github-Time-Tracking](https://github.com/StephenOTT/GitHub-Time-Tracking#time-tracking-usage-patterns)
for tracking time and budget spent on project.

## Installation
    pip install git+https://github.com/rdev-hackaton/GitHubTimeTracker
## Usage

### CLI
To get list of all commit entries in your project call GitHubTimeTracker with address to your repository. For more specific data use flags.

    $ ghtt
    Github login or personal access token:
    $ myusername
    Github password:
    $ mypassword
    Repo name:
    $ GitHubTimeTracker #input your repository name

You may provide your repository address inline. If you don't, GitHubTimeTracker will ask you for it explicitely.

    --repo repoName

You may get info about specific commiter, issue and milestone.

    --commiter username

    --issue numberOfIssue

    --milestone

If you want to get total time and budget of your request use total flag.

    --total

## Time logging

You can tag your activities with the amount of time spent on them by adding a simple prefix. Here are a few examples:

    :clock1: 15m | Initial research
    :clock12: 2h 30m | Fix the javascript error on iOS / safari
    :clock5: 4d16h Yak shaving

The line should begin with the `:clock1:` bit - pick any clock emoji you like - and then be followed by `Xd`, `Xh` or `Xm` for days, hours and minutes. The pipe symbol is optional, but strongly recommended as it provides a visual separation between the time log and the comment.

You can use this syntax to log time spent on commits, issues, pull requests and so forth.

## Authors

[<img alt="Marek Bednarski" src="https://avatars2.githubusercontent.com/u/13423250" height="60px">](https://github.com/b-me)
[<img alt="Filip Figiel" src="https://avatars1.githubusercontent.com/u/4096683" height="60px">](https://github.com/megapctr)
[<img alt="Łukasz Haze" src="https://avatars1.githubusercontent.com/u/2180285" height="60px">](https://github.com/lhaze)
[<img alt="Łukasz Kożuchowski" src="https://avatars3.githubusercontent.com/u/1458848" height="60px">](https://github.com/evalapply)
[<img alt="Piotr Pęczek" src="https://avatars0.githubusercontent.com/u/2931838" height="60px">](https://github.com/ppeczek)
[<img alt="Jakub Skałecki" src="https://avatars3.githubusercontent.com/u/3935986" height="60px">](https://github.com/Valian)
