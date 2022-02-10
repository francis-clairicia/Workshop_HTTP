#!/usr/bin/env python
"""
Exercice:

Make a GET request on https://httpbin.org/status/{expected_status} and show the response status code

For example, if 'expected_status' has value 200, the URL link will be https://httpbin.org/status/200

(To see the complete list of HTTP response codes and their meanings: https://umbraco.com/knowledge-base/http-status-codes/)

(There is no response body for that request)
"""

import argparse
import requests


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch ./ex02 -h  :)")
    parser.add_argument("status", type=int, nargs="?", default=200, help="The status code to send")

    expected_status = parser.parse_args().status

    return


if __name__ == "__main__":
    main()
