#!/usr/bin/env python
"""
Exercice:

Make a POST request on http://httpbin.org/post, sending the 'data' object, and show the received JSON payload.

You must see the same data in response in 'form' object
"""

import requests


def main() -> None:
    data = {
        "username": "John Doe",
        "password": "the-best-john-doe"
    }

    return


if __name__ == "__main__":
    main()
