#!/usr/bin/env python
"""
Exercice:

Show your Github profile.

(Github API documentation: https://docs.github.com/en/rest/reference)

You must see in the terminal (the information between curly bracket must be taken from response body):
- Username: {string}
- Full name: {string}
- Email: {string}
- Owned public repositories: {number}
- Owned private repositories: {number}
"""

from github import GithubSession

with open("github.token") as _F:
    GITHUB_TOKEN = _F.read()

del _F

SESSION = GithubSession(GITHUB_TOKEN)

print(SESSION.auth)  # You should see your token


def main() -> None:
    return


if __name__ == "__main__":
    main()
