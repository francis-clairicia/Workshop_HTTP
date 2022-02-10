#!/usr/bin/env python
"""
Exercice:

Show one of your repositories.

You must see in the terminal:
- Repository name: {string}
- Creation date: {string}
- Owner: {string}
- Description: {string} if there is one
- Private?: {boolean}
- Repository language: {string}
"""

from github import GithubSession

with open("github.token") as _F:
    GITHUB_TOKEN = _F.read()

del _F

SESSION = GithubSession(GITHUB_TOKEN)


def main() -> None:
    return


if __name__ == "__main__":
    main()
