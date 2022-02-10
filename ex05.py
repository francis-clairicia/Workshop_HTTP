#!/usr/bin/env python
"""
Exercice:

Show your Epitech organization (EpitechPromo2024 for example).

You must have configure the SSO with your personal access token to see the information.

You must see in the terminal:
- Organisation name: {string}
- Owned public repositories: {number}
- Owned private repositories: {number}
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
