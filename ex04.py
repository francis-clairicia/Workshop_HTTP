#!/usr/bin/env python
"""
Exercice:

Show MY Github profile (francis-clairicia) with the same format as ex03.
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
