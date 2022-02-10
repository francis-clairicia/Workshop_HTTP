# -*- coding: Utf-8 -*

from requests import Session, PreparedRequest
from requests.auth import AuthBase


class GithubAuth(AuthBase):
    def __init__(self, token: str) -> None:
        super().__init__()
        self.token: str = token

    def __repr__(self) -> str:
        return f"<Github Authorization token={self.token}>"

    __str__ = __repr__

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


class GithubSession(Session):
    def __init__(self, token: str) -> None:
        super().__init__()
        self.auth = GithubAuth(token)
        self.headers["Accept"] = "application/vnd.github.v3+json"
