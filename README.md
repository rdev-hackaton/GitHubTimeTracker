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

    $ ghttracker
    Repo address (url or local path):
    $ https://github.com/...
    
You may provide your repository address inline. If you don't, GitHubTimeTracker will ask you for it explicitely.

    --repo repoAddress

You may get info about specific commiter, issue and milestone.

    --commiter username

    --issue numberOfIssue
    
    --milestone
    
If you want to get total time and budget of your request use total flag.

    --total

## Authors
[![Marek Bednarski](https://avatars2.githubusercontent.com/u/13423250?v=3&s=60)](https://github.com/b-me)
[![Filip Figiel](https://avatars1.githubusercontent.com/u/4096683?v=3&s=60)](https://github.com/megapctr)
[![Łukasz Haze](https://avatars1.githubusercontent.com/u/2180285?v=3&s=60)](https://github.com/lhaze)
[![Łukasz Kożuchowski](https://avatars3.githubusercontent.com/u/1458848?v=3&s=60)](https://github.com/evalapply)
[![Piotr Pęczek](https://avatars0.githubusercontent.com/u/2931838?v=3&s=60)](https://github.com/ppeczek)
[![Jakub Skałecki](https://avatars3.githubusercontent.com/u/3935986?v=3&s=60)](https://github.com/Valian)
