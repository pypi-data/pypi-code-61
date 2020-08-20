#!/usr/bin/env python3
#
# Usage: .py
#

import writeas
from datetime import datetime
import sys


def main():
    credential_file = sys.argv[1]
    output_file = sys.argv[2]

    username, password = get_credentials(credential_file)

    c = writeas.client()
    user = c.login(username, password)

    c.setToken(user['access_token'])

    posts = c.retrievePosts()

    # Get posts in reversed order (from newest to oldest)
    with open(output_file, mode="w", encoding='utf-8') as output:
        for post in posts[::-1]:
            post_title = post["title"]
            post_id = post["slug"]
            post_views = str(post["views"])
            post_created = datetime.fromisoformat(post["created"][:-1]).strftime("%d.%m.%Y")
            output.write(f"{post_title},{post_created},{post_id},{post_views}\n")


def get_credentials(credential_file):
    with open(credential_file, mode="r", encoding='utf-8') as file:
        lines = file.readlines()
        return lines[0], lines[1]


if __name__ == '__main__':
    main()
