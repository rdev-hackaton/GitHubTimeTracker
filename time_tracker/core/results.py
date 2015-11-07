from enum import Enum


class Result(Enum):
    OK = 200
    REPO_NOT_FOUND = 404
    ISSUE_NOT_FOUND = 405
    COMMITTER_NOT_FOUND = 406
