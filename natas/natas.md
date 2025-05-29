# Natas
https://overthewire.org/wargames/natas/

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in /etc/natas_webpass/. E.g. the password for natas5 is stored in the file /etc/natas_webpass/natas5 and only readable by natas4 and natas5.


## 0
Start here:

Username: natas0
Password: natas0
URL:      http://natas0.natas.labs.overthewire.org


## 0->1
http://natas0.natas.labs.overthewire.org/

Solved by accessing Chrome Dev Tools and looking at DOM.

<img width="2137" alt="Screenshot 2025-05-28 at 6 33 45 PM" src="https://github.com/user-attachments/assets/4eba0538-2380-4285-b6a0-2828da22cbf8" />
`<!--The password for natas1 is 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq -->`

