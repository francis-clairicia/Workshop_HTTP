#!/usr/bin/env python
"""
Exercice:

For the repository you previously chosen, show the last commit.

You must see in the terminal:
- Commit hash: {string}
- Author name: {string}
- Author email: {string}
- Committer name: {string}
- Committer email: {string}
- Message: {string}
- Number of comments: {number}
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
