from enum import Enum


class Result(Enum):
    OK = 200
    REPO_NOT_FOUND = 404
    ISSUE_NOT_FOUND = 405
    COMMITER_NOT_FOUND = 406
