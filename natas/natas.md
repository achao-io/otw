# Natas
- https://overthewire.org/wargames/natas/

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in /etc/natas_webpass/. E.g. the password for natas5 is stored in the file /etc/natas_webpass/natas5 and only readable by natas4 and natas5.

## 0
- http://natas0.natas.labs.overthewire.org
- `natas0:natas0`

## 0->1
- http://natas0.natas.labs.overthewire.org/
- `natas1:0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq`
- Solved by accessing Chrome Dev Tools and looking at DOM.

<img width="2137" alt="Screenshot 2025-05-28 at 6 33 45 PM" src="https://github.com/user-attachments/assets/4eba0538-2380-4285-b6a0-2828da22cbf8" />

## 1->2
- http://natas1.natas.labs.overthewire.org/
- `natas2:TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI`
- Right clicking was blocked, but F12 gets me to Dev Tools.

<img width="2229" alt="Screenshot 2025-05-28 at 6 36 20 PM" src="https://github.com/user-attachments/assets/a8c112fe-438e-400d-92a3-5843ad49425e" />

## 2->3
- http://natas2.natas.labs.overthewire.org/
- `natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH`
- This one involved realizing that there exists an accessible `file` directory at `http://natas2.natas.labs.overthewire.org/files`. In this directory, there is a file `users.txt` with the natas3 password.

<img width="2242" alt="Screenshot 2025-05-28 at 6 39 16 PM" src="https://github.com/user-attachments/assets/3265201d-3a7e-40a9-8fa0-3083db36a802" />
<img width="2241" alt="Screenshot 2025-05-28 at 6 46 19 PM" src="https://github.com/user-attachments/assets/bc04e8b5-66f3-432b-b313-941ee6a26e9d" />
<img width="563" alt="Screenshot 2025-05-28 at 6 47 40 PM" src="https://github.com/user-attachments/assets/03250a35-1686-4dfe-98f8-43a84483c88d" />
<img width="619" alt="Screenshot 2025-05-28 at 6 47 54 PM" src="https://github.com/user-attachments/assets/197b3680-1cb0-40a1-9e53-f9d8951c2a23" />


## 3->4
- http://natas3.natas.labs.overthewire.org/
- `natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ`
> What is robots.txt?
> 
> https://en.wikipedia.org/wiki/Robots.txt
> A robots.txt file is a plain text file that tells web crawlers, also known as spiders or bots, how they should crawl a website. It's essentially a set of instructions that specify which parts of a website should be accessed by crawlers and which should be excluded.

<img width="598" alt="Screenshot 2025-05-28 at 7 07 41 PM" src="https://github.com/user-attachments/assets/7b2d63c6-b2be-47e1-b1a9-7d2e8a84afd7" />
<img width="557" alt="Screenshot 2025-05-28 at 7 08 03 PM" src="https://github.com/user-attachments/assets/1d516330-1914-4713-8537-b6d35c7d7f13" />
<img width="615" alt="Screenshot 2025-05-28 at 7 08 15 PM" src="https://github.com/user-attachments/assets/28efd70b-e816-49c4-94d6-d01408f6d941" />
