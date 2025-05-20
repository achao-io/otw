# bandit

## 0
https://overthewire.org/wargames/bandit/bandit0.html
- `ssh <url> --login/-l <user> --port/-p XXXX`
- `ssh bandit.labs.overthewire.org -l bandit0 -p 2220`


## 1
https://overthewire.org/wargames/bandit/bandit1.html
- `ssh bandit.labs.overthewire.org -l bandit1 -p 2220`
- ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## 2
https://overthewire.org/wargames/bandit/bandit2.html
- `more -`
- 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
why does more - work, but less - doesn't work?
The difference in behavior between more - and less - is due to how these commands handle the hyphen (-) argument:

1. more - works because it treats the hyphen (-) as indicating to read from standard input (stdin)
2. less - doesn't work by default because it interprets the lone hyphen differently - it tries to treat it as an invalid option flag

To make less read from stdin like more does, you need to use either:
•  less < - (redirect input)
•  less ./- (explicitly reference the current directory)
•  Or pipe content to it: cat - | less

This is particularly relevant when dealing with files that start with a hyphen, as the hyphen can be misinterpreted as a command option. This is a common security consideration when handling files, which is why using './-' or similar explicit path references is considered a good practice.
```

## 3
https://overthewire.org/wargames/bandit/bandit3.html
- `more ~/"spaces in this filename"`
- MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## 4
https://overthewire.org/wargames/bandit/bandit4.html
```
The password for the next level is stored in a hidden file in the inhere directory.
```
```
% ls
% cd inhere
% ls -alh
% cat ...Hiding-From-You
```
- 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## 5
https://overthewire.org/wargames/bandit/bandit5.html
```
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.
```
```
% for file in ./-file*; do
    echo "=== $file ==="
    cat "$file"
done

=== ./-file00 ===
�ŉOT���S �plS]-EH�t�:-�Z�
                         === ./-file01 ===
N$���'���Se��
             \�- V�P�jls�����=== ./-file02 ===

o5e�Mz9�#P�ws������Oh||xt��=== ./-file03 ===
6|ر��Vܒ��q ��*rMӼ^';b\�=== ./-file04 ===

x����]C�
        �H`�/�X���OGLV=== ./-file05 ===
��*��-o��w9�P�RAz�b��[��F�=== ./-file06 ===
��_��+J��2X1�M�O�g��Y����d�Ŧj=== ./-file07 ===
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
=== ./-file08 ===
t=== ./-file09 ===
)�r�R�C#�ӧ��4��_�\����^�)C
```

## 6
https://overthewire.org/wargames/bandit/bandit6.html
```
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable
```bash
- `find ~/inhere -type f -size 1033c`
```
what other options are there for the "c" in -size 1033c?
The size suffixes available in the find command are:
c for bytes
k for kilobytes
M for megabytes
G for gigabytes
b for 512-byte blocks (default if no suffix)
w for 2-byte words
```

```bash
bandit5@bandit:~/inhere$ find ~/inhere -type f -size 1033c
/home/bandit5/inhere/maybehere07/.file2
bandit5@bandit:~/inhere$ cat /home/bandit5/inhere/maybehere07/.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

## 7
https://overthewire.org/wargames/bandit/bandit7.html
```
The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size
```
```bash
% find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null
/var/lib/dpkg/info/bandit7.password
% cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```
- `2> /dev/null` redirects error messages to the null device, hiding them. Cleaner output. 

## 8
https://overthewire.org/wargames/bandit/bandit8.html
```
The password for the next level is stored in the file data.txt next to the word millionth
```
```bash
% grep millionth data.txt 
millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

## 9
https://overthewire.org/wargames/bandit/bandit9.html
```
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once
```
- tried `cat data.txt | uniq -u` first, but didn't work. This is because `uniq` only removes consecutive duplicate lines. If duplicate lines are not adjacent, `uniq` won't consider them duplicates. To make sure identical lines are next to each other, `sort` the file first.
```bash
% sort data.txt | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```

## 10
https://overthewire.org/wargames/bandit/bandit10.html
```
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
```

**How can I `cat data.txt` and extract "human readable strings"?**

You can use the `strings` command on the file. The `strings` command extracts sequences of printable characters from a file. In your case, try running:

`strings data.txt`

This will output all human-readable strings from `data.txt`. If you want to specifically see lines starting with several '=' characters, you can combine it with `grep`, for example:

`strings data.txt | grep '^==='`

Adjust the number of '=' in your grep pattern to suit the expected number of preceding '=' characters.

**why do you need the carot in front of the grep search string? e.g. `grep ''^==='`**

The caret (^) in a grep search pattern is used as an anchor to match the beginning of the line. When you write `grep '^==='` it tells `grep` to only look for lines that start with "===", rather than matching "===" anywhere within the line. This is useful if you're trying to extract or filter lines that have a specific format where the characters should appear at the start.

```bash
% strings data.txt | grep "=="
========== the
========== password{k
=========== is
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

## 11
https://overthewire.org/wargames/bandit/bandit11.html
```
The password for the next level is stored in the file data.txt, which contains base64 encoded data
```
```bash
% base64 -d data.txt
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

## 12
https://overthewire.org/wargames/bandit/bandit12.html
```
The password for the next level is stored in the file data.txt, where all 
lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
```
- use `tr` to handle char rotation
```bash
% cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
```
--
ROT13 Character Mapping
'A-Za-z' represents the input character set (all letters A to Z, both uppercase and lowercase)
'N-ZA-Mn-za-m' represents the output character set where each letter is shifted 13 positions forward
The mapping works by:
A→N, B→O, ..., M→Z, N→A, ..., Z→M (uppercase)
a→n, b→o, ..., m→z, n→a, ..., z→m (lowercase)
```

## 13
https://overthewire.org/wargames/bandit/bandit13.html
```
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Commands you may need to solve this level
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file
```
xxd might be useful here...

DESCRIPTION
       xxd  creates  a  hex dump of a given file or standard input.  It can also convert a hex dump back to its original binary
       form.  Like uuencode(1) and uudecode(1) it allows the transmission of binary data in a `mail-safe' ASCII representation,
       but has the advantage of decoding to standard output.  Moreover, it can be used to perform binary file patching.

       -r | -revert
              Reverse operation: convert (or patch) hex dump into binary.  If not writing to stdout, xxd writes into its output
              file  without truncating it. Use the combination -r -p to read plain hexadecimal dumps without line number infor‐
              mation and without a particular column layout. Additional whitespace and line breaks are  allowed  anywhere.  Use
              the combination -r -b to read a bits dump instead of a hex dump.

```bash
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ cat data.txt 
00000000: 1f8b 0808 41d4 f767 0203 6461 7461 322e  ....A..g..data2.
00000010: 6269 6e00 0149 02b6 fd42 5a68 3931 4159  bin..I...BZh91AY
00000020: 2653 59a8 ffa7 8f00 001d 7fff dbeb 7ffa  &SY.............
00000030: bb7f a5ef bb7e f5fb fdff b7c7 f3ff ff7f  .....~..........
00000040: ff7f fff7 deba fdfa eff7 dddf b001 3b19  ..............;.
00000050: a200 d01a 0190 0034 0006 800d 0340 0346  .......4.....@.F
00000060: 8000 0340 0320 0069 a034 0640 0346 4680  ...@. .i.4.@.FF.
00000070: 68d1 a68c 8321 9313 4da4 f510 6406 8003  h....!..M...d...
00000080: 4006 9a00 000d 000d 0069 a007 a9a0 001a  @........i......
00000090: 1b50 03d4 01a6 9a1e a001 a343 4683 469a  .P.........CF.F.
000000a0: 3d40 001a 7a8d 01a0 074c 801e a1a6 8064  =@..z....L.....d
000000b0: 01a3 d434 00c4 0d00 000d 0001 a680 1a19  ...4............
000000c0: 0061 0f53 41a0 0000 0d00 341a 0320 0034  .a.SA.....4.. .4
000000d0: d1ea 0168 4882 8244 0130 5550 f16b f52e  ...hH..D.0UP.k..
000000e0: a322 cb9f bb8c aaf6 e244 cc70 b151 47c8  .".......D.p.QG.
000000f0: 6c03 a3ae 4a81 1ee0 03ce 840e a978 2046  l...J........x F
00000100: 630b 4b0d 9883 7078 e7e8 5bfb 68f1 f685  c.K...px..[.h...
00000110: 6f46 771c 3920 449f f0cb 39e2 0841 10b5  oFw.9 D...9..A..
00000120: 8714 e981 115c d1bc 2da4 318b 106c 904e  .....\..-.1..l.N
00000130: 9328 5e97 405a 4054 21db e049 1a32 5f3d  .(^.@Z@T!..I.2_=
00000140: 7069 408f f0a4 8ce5 fbea 282c 51d1 49e4  pi@.......(,Q.I.
00000150: d52f 0762 dd90 27b8 79d3 0499 52e0 060c  ./.b..'.y...R...
00000160: fd91 a474 d408 88f3 1fda d2d1 325a baeb  ...t........2Z..
00000170: bfe7 f0f6 cc3c 776d f369 e73c 47d4 66ea  .....<wm.i.<G.f.
00000180: 4b90 e404 03b3 6a09 4687 945d 09ef 706b  K.....j.F..]..pk
00000190: 8f82 2503 80d0 0a0a 3e60 f879 bf02 2d42  ..%.....>`.y..-B
000001a0: bf37 9c96 4b22 585c 35c8 3cf1 da9f 518b  .7..K"X\5.<...Q.
000001b0: ccd5 a68c 9647 aa38 8a50 89d2 f89c 1ff0  .....G.8.P......
000001c0: 1042 18c3 6549 400d fe17 ec74 3171 6d74  .B..eI@....t1qmt
000001d0: a8bb 0def f11a 5a69 0e70 aa34 0037 b180  ......Zi.p.4.7..
000001e0: 1540 c4d2 0af7 e290 8784 ce9e 147a 6836  .@...........zh6
000001f0: 944b 3f18 2ba2 c620 af92 fb01 184f 3def  .K?.+.. .....O=.
00000200: 1b7d 0162 733d adca 90ac 7142 8319 f703  .}.bs=....qB....
00000210: 5930 69e2 8320 9110 5d63 0db9 9294 d4ef  Y0i.. ..]c......
00000220: 50b9 5907 0924 92c1 014e a284 25ce a6ef  P.Y..$...N..%...
00000230: 67b2 4e06 6d21 4136 2ac0 292d 6638 033c  g.N.m!A6*.)-f8.<
00000240: 21af be4e 13bb b74f 2c10 18c7 eea3 c436  !..N...O,......6
00000250: c988 05e6 5638 1ff1 7724 5385 090a 8ffa  ....V8..w$S.....
00000260: 78f0 d951 192d 4902 0000                 x..Q.-I...
```

hex > binary
```bash
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ xxd -r data.txt 
4 4��hH��D0UP�k�.�"˟�����D�p�QG�l��J��΄�x Fc������޺�����߰;���4�
��px��[�h���oFw9 D���9A���\Ѽ-�1�l�N�(^�@Z@T!��I2_=pi@�����(,Q�I��/bݐ'�y��R�
                                                                           ���t�����2Z������<wm�i�<G�f�K���j    F��]    �pk��%��

��Zip�47��@��X\5�<�ڟQ��զ��G�8�P�����B�eI@
�����P�YK?+�� ��$��N��%Φ�g�Nm!A6*�)-f8<!��N��O,���6Ɉ�V8�w$S�
```

now to uncompress... gzip? bzip2? tar? checking man pages

```bash
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ xxd -r data.txt > output.bin
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ ls
data.txt  output.bin  -r
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ vim output.bin 
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ cat output.bin 
A��gdata2.binI��BZh91AY&SY�����������~�����������4 4��hH��D0UP�k�.�"˟�����D�p�QG�l��J��΄�x Fc
��px��[�h���oFw9 D���9A���\Ѽ-�1�l�N�(^�@Z@T!��I2_=pi@�����(,Q�I��/bݐ'�y��R�
                          ���t�����2Z������<wm�i�<G�f�K���j      F��]    �pk��%��

��Zip�47��@��X\5�<�ڟQ��զ��G�8�P�����B�eI@
�����P�YK?+�� ��$��N��%Φ�g�Nm!A6*�)-f8<!��N��O,���6Ɉ�V8�w$S�
```

you can find out useful information about a file with `file`

```bash
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ file output.bin
output.bin: gzip compressed data, was "data2.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 585
```

so gzip

```bash
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ gzip -d output.bin
gzip: output.bin: unknown suffix -- ignored
```

problem is, gzip is expecting a file ending with `.gz`. so, use `-f` or add the `.gz` extension

``
wow, that was like 8 layers deep of `gzip -d`, `bzip2 -d`, `tar xvf`. Each step using `file` to understand what compression was used. Make sure file extension for `gzip` ends in `gz` and `bzip2` ends in `bz2`.

here is the work: https://gist.github.com/achao-io/4e14b332f67d80a12a612e6329d0bb1f

```bash
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ file data8.bin
data8.bin: ASCII text
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ cat data8.bin
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

## 14
https://overthewire.org/wargames/bandit/bandit14.html
```
Level Goal
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

Commands you may need to solve this level
ssh, telnet, nc, openssl, s_client, nmap

Helpful Reading Material
SSH/OpenSSH/Keys
```

Tools to learn...
`ssh` - ssh (SSH client) is a program for logging into a remote machine and for executing commands on a remote machine.   It  is intended  to  provide secure encrypted communications between two untrusted hosts over an insecure network.  X11 connections, arbitrary TCP ports and Unix-domain sockets can also be forwarded over the secure channel.
telnet - 
nc
openssl
s_client
nmap

-i identity_file
        Selects  a file from which the identity (private key) for public key authentication is read.  You can also spec‐ify a public key file to use the corresponding private key that is loaded in ssh-agent(1) when the  private  key file   is   not   present   locally.    The   default  is  ~/.ssh/id_rsa,  ~/.ssh/id_ecdsa,  ~/.ssh/id_ecdsa_sk, ~/.ssh/id_ed25519, ~/.ssh/id_ed25519_sk and ~/.ssh/id_dsa.  Identity files may also be specified on  a  per-host basis  in the configuration file.  It is possible to have multiple -i options (and multiple identities specified in configuration files).  If no certificates have been explicitly specified by  the  CertificateFile  directive, ssh  will also try to load certificate information from the filename obtained by appending -cert.pub to identity
        filenames.

```bash
bandit13@bandit:~$ ssh bandit.labs.overthewire.org -l bandit14 -p 2220 -i sshkey.private
```

## 15
https://overthewire.org/wargames/bandit/bandit15.html
```
Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
```
```bash
bandit14@bandit:/etc/bandit_pass$ pwd
/etc/bandit_pass
bandit14@bandit:/etc/bandit_pass$ cat bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

what does it mean to "submit the password to port 30000 on localhost"? foreign terminology to me.

Analogy from Cursor: "Think of it like knocking on a specific door (port 30000) of your house (localhost) and saying a password to get a response back."


```bash
nc localhost 30000
telnet localhost 30000
```

what are these two commands "doing"?

```
Both nc (netcat) and telnet are network communication tools that establish a connection to a specified host and port. In this case, they're both trying to connect to port 30000 on localhost (your own machine). Here's what each does:

nc localhost 30000 (netcat):
- Creates a TCP connection to port 30000 on localhost
- Opens a simple, raw connection where you can send and receive text
- More modern and versatile tool
- Often used for debugging, testing, and simple network connections
- After connecting, you can type the password and press Enter to send it

telnet localhost 30000:
- Also creates a connection to port 30000 on localhost
- Originally designed for interactive terminal sessions
- Older protocol but still useful for testing TCP connections
- After connecting, you can type the password and press Enter to send it

The main difference is that:
- nc is a more modern, versatile tool that can handle both TCP and UDP connections
- telnet is an older protocol primarily designed for interactive terminal sessions

In this specific challenge, either command will work because you just need to:
- Establish a connection to port 30000
- Send the password
- Receive the response

Think of both commands like picking up a phone (establishing a connection) to call a specific extension (port 30000) in your own building (localhost), where you'll then speak the password and get a response back.
```

okay here we go

```bash
bandit14@bandit:/etc/bandit_pass$ pwd
/etc/bandit_pass
bandit14@bandit:/etc/bandit_pass$ cat bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
bandit14@bandit:/etc/bandit_pass$ nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

## 16
https://overthewire.org/wargames/bandit/bandit16.html
```
Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

Commands you may need to solve this level
ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss

Helpful Reading Material
[Secure Socket Layer/Transport Layer Security on Wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)
[OpenSSL Cookbook - Testing with OpenSSL](https://www.feistyduck.com/library/openssl-cookbook/online/testing-with-openssl/index.html)
```

can I do it with just `nc`?

```
No, you cannot use plain nc (netcat) for this task, because nc only creates unencrypted (plain TCP) connections. The challenge specifically requires you to use SSL/TLS encryption to connect to port 30001.

To connect using SSL/TLS, you should use a tool that supports encrypted connections, such as:
- openssl s_client
- ncat (with the --ssl option, if available)
- socat (with appropriate options)
The most common and portable way is:

% openssl s_client -connect localhost:30001

Then, once connected, paste or type the password and press Enter.

Summary:
- nc = plain, unencrypted TCP (not suitable for SSL/TLS)
- openssl s_client = encrypted SSL/TLS connection (what you need here)
If you try with nc, the server will not understand your request because it expects an encrypted handshake, not plain text. 
```

```bash
2025-05-03 Other Options

- openssl s_client is the most universal and low-level tool for this.
- ncat and socat are great alternatives if installed.
- Scripting (Python, etc.) is useful for automation.
- curl is only for HTTP(S) services.

| Tool/Method | Command/Usage Example | Notes |
|---------------------|-------------------------------------------------------|------------------------------|
| openssl s_client | openssl s_client -connect localhost:30001 | Most common |
| ncat | ncat --ssl localhost 30001 | Modern netcat with SSL |
| socat | socat - OPENSSL:localhost:30001,verify=0 | Very flexible |
| Python (ssl) | See script above | Good for automation |
| curl | curl -k https://localhost:30001 | Only for HTTP(S) protocols |
```

```bash
bandit15@bandit:~$ openssl s_client localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 266436B3C1C32EEAB434045CC80CBA16021CE6C475D32BB653957E1BC9126745
    Session-ID-ctx: 
    Resumption PSK: A1EF6E99FBD612041625CF6D517A8FFC6B69C2A2DEE130465B4FC948D600F6B29E0B3B2B2EF64E96FB4985AC1F2757EC
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 14 8e 4f dd d3 b0 a2 87-64 84 21 86 93 29 46 0d   ..O.....d.!..)F.
    0010 - 37 a6 2a 47 8a 70 9b 9e-a6 7c a2 1e ca 11 09 4d   7.*G.p...|.....M
    0020 - 85 73 27 13 32 e6 68 59-e7 9f 8c 94 69 70 4d 01   .s'.2.hY....ipM.
    0030 - a3 bd 76 be 20 a3 be 56-23 24 12 e6 91 e8 d9 b9   ..v. ..V#$......
    0040 - f6 71 72 27 bd 2e 4a bb-2e 3d f5 36 33 d8 de 91   .qr'..J..=.63...
    0050 - 75 7f e7 b1 c8 ac 5d c3-a5 d8 16 df c4 3e 9a 07   u.....]......>..
    0060 - 41 fa 91 7c c7 bb 08 37-40 c6 d4 81 96 20 a9 23   A..|...7@.... .#
    0070 - 9d 82 e9 8e a2 ec 43 69-1a 79 56 e7 89 4c 88 45   ......Ci.yV..L.E
    0080 - b8 1e d6 63 d5 a6 68 13-18 50 6c 9b 77 3e e2 80   ...c..h..Pl.w>..
    0090 - 3b 9f 3a 35 df ad 9e c1-1e 50 72 f6 c3 36 37 25   ;.:5.....Pr..67%
    00a0 - fc bd 61 77 48 29 fc a1-0d 79 f9 ef 1f 5c 32 cb   ..awH)...y...\2.
    00b0 - 84 8a 5b 38 00 7f f3 92-5b 78 6d 38 07 9f fd 3f   ..[8....[xm8...?
    00c0 - 01 36 07 fb db ff 5b d5-eb 64 f1 04 6d bd ae d7   .6....[..d..m...
    00d0 - ba 5c cf 75 4b c6 8c 98-c0 9f a9 39 fc 33 1c 42   .\.uK......9.3.B

    Start Time: 1746240452
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 8D9792C62713DE60BAE7F50ECFA0851728DF197032EE8AFB0A783534682C3D48
    Session-ID-ctx: 
    Resumption PSK: 7EEE828704F4171BA10F31511D49345142CE071818B3EF055CC8615D61387DAAD77E9B04EA7527DEBA459F0C3DADD0F6
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 14 8e 4f dd d3 b0 a2 87-64 84 21 86 93 29 46 0d   ..O.....d.!..)F.
    0010 - 4e f1 a2 b4 2f 01 a7 39-d6 f4 4a 92 8e cf cc b0   N.../..9..J.....
    0020 - 47 3c 14 65 6a d7 ba 72-87 c2 4e e3 1f 30 43 d1   G<.ej..r..N..0C.
    0030 - 5c 2b e5 35 5b b4 44 b4-33 f6 74 07 4c d0 3c 0d   \+.5[.D.3.t.L.<.
    0040 - c7 b6 ce a6 98 43 f7 75-81 ed 4f 09 2e 62 ff f4   .....C.u..O..b..
    0050 - 2e bb ee 8a 4b 78 84 75-f1 1e fd 90 cd 81 35 7e   ....Kx.u......5~
    0060 - 0a 75 ab 8a 79 26 f7 c0-5b 0e 3b c0 2b 0b 4d 64   .u..y&..[.;.+.Md
    0070 - f1 68 46 83 c8 e3 5d 39-26 47 a5 4d ba b8 74 64   .hF...]9&G.M..td
    0080 - 3e 40 27 ed 49 06 61 51-d0 6e f7 b6 97 0a 02 18   >@'.I.aQ.n......
    0090 - 91 a0 dd aa 77 7f d0 3e-19 05 a0 b3 46 43 8e f2   ....w..>....FC..
    00a0 - d3 f2 bf 5e 7a 62 52 44-62 2c c8 5c 95 f1 17 8d   ...^zbRDb,.\....
    00b0 - 02 19 86 0d 88 2c ec 0c-4b 29 6a e4 02 43 a4 72   .....,..K)j..C.r
    00c0 - 7c 20 38 76 f7 1b 5f 26-b8 53 d1 29 a1 82 3d d3   | 8v.._&.S.)..=.
    00d0 - e4 b2 d9 e3 e1 87 f9 32-3e b5 16 4c 6d 1d 48 74   .......2>..Lm.Ht

    Start Time: 1746240452
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed
```

## 17
```
https://overthewire.org/wargames/bandit/bandit17.html
Level Goal
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

Commands you may need to solve this level
ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss

Helpful Reading Material
[Port scanner on Wikipedia](https://en.wikipedia.org/wiki/Port_scanner)
```

[nmap](https://nmap.org/)! super powerful network mapper. used all the time in movies/media. very cool.

```bash
bandit16@bandit:~$ nmap -p 31000-32000 localhost 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-05-03 23:26 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00015s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
bandit16@bandit:~$ ncat --ssl local 31046
test
Ncat: Could not resolve hostname "local": Temporary failure in name resolution. QUITTING.
bandit16@bandit:~$ test
bandit16@bandit:~$ ncat --ssl localhost 31046
Ncat: Input/output error.
bandit16@bandit:~$ ncat --ssl localhost 31518
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
^C
bandit16@bandit:~$ ncat --ssl localhost 31691
Ncat: Input/output error.
bandit16@bandit:~$ ncat --ssl localhost 31790
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

> Is there a smarter way to do this than to brute force the ports nmap found?

**Short answer:**  
For this specific Bandit level, brute-forcing the handful of open ports is actually the intended and most practical approach, because:

- The challenge is designed to teach you about port scanning and protocol detection.
- There are only a few open ports in the range (5 in your example), so it’s not a true brute-force of thousands of ports.
- There’s no advertised protocol or banner to distinguish the correct service without trying to connect.

---

## Why brute-forcing is “smart” here

- **nmap** tells you which ports are open, but not which ones use SSL/TLS or which one is the “real” service.
- The only way to know which port expects SSL/TLS and gives the next password is to try connecting (with `ncat --ssl`, `openssl s_client`, etc.) and see the response.
- The “dumb” brute-force would be to try all 1001 ports; the “smart” brute-force is to scan, then try only the 5 open ones.

---

## Can you automate it?

Yes! You can script the process to make it less manual. For example, here’s a bash one-liner to try all open ports with `ncat --ssl` and send the password:

```bash
for port in 31046 31518 31691 31790 31960; do
  echo "Trying port $port"
  echo "YOUR_PASSWORD_HERE" | ncat --ssl localhost $port
done
```
Or, to automate the nmap scan and test each open port:

```bash
for port in $(nmap -p31000-32000 --open -T4 -oG - localhost | grep '/open/' | awk '{print $2}' | tr ',' '\n'); do
  echo "Trying port $port"
  echo "YOUR_PASSWORD_HERE" | ncat --ssl localhost $port
done
```

---

## Is there a way to distinguish the correct port without connecting?

- **Not reliably.**  
  - nmap’s service detection (`-sV`) might sometimes help, but for custom or minimal services (like in Bandit), it usually just says “unknown.”
  - You could try banner grabbing with plain `nc` or `telnet`, but if the service expects SSL/TLS, you’ll just get gibberish or nothing.
  - Only by actually connecting with SSL/TLS and sending the password will you know for sure.

---

## Summary

- **Brute-forcing** the small set of open ports is the intended and most efficient approach for this challenge.
- You can automate it with a script to make it less tedious.
- There’s no “smarter” way in the sense of avoiding trying each port, unless the service gives away a unique banner (which it doesn’t here).

**In real-world scenarios, you might use more advanced fingerprinting, but for Bandit, this is the right approach!**

---

How can I use the RSA Private Key to get to the next level?

Something like bandit 13->14
```
bandit13@bandit:~$ ssh bandit.labs.overthewire.org -l bandit14 -p 2220 -i sshkey.private
```

`mktemp`!
```
Create  a temporary file or directory, safely, and
       print its name.  TEMPLATE must contain at least  3
       consecutive  'X's  in last component.  If TEMPLATE
       is not specified, use tmp.XXXXXXXXXX, and --tmpdir
       is implied.  Files are created u+rw, and  directo‐
       ries u+rwx, minus umask restrictions.
```

```
bandit16@bandit:~$ mktemp
/tmp/tmp.qkTYdDP8Ff
bandit16@bandit:~$ man mktemp
bandit16@bandit:~$ vim /tmp/tmp.qkTYdDP8Ff
bandit16@bandit:~$ ssh -i /tmp/tmp.qkTYdDP8Ff bandit17@bandit.labs.overthewire.org -p 2220
```

Got in!

## 18
https://overthewire.org/wargames/bandit/bandit18.html
```
Level Goal
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

Commands you may need to solve this level
cat, grep, ls, diff
```

```bash
bandit17@bandit:~$ l
passwords.new  passwords.old
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.new passwords.old 
42c42
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> C6XNBdYOkgt5ARXESMKWWOUwBeaIQZ0Y
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< C6XNBdYOkgt5ARXESMKWWOUwBeaIQZ0Y
---
> x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```

## 19
https://overthewire.org/wargames/bandit/bandit19.html
```
Level Goal

The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

Commands you may need to solve this level
ssh, ls, cat
```

TIL: You can run a single command on a remote server via SSH without starting an interactive shell.

```bash
otw git:(main) ✗ ssh bandit.labs.overthewire.org -l bandit18 -p 2220 "cat readme"
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```

## 20
https://overthewire.org/wargames/bandit/bandit20.html
```
Level Goal
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
```

https://en.wikipedia.org/wiki/Setuid

What is  `setuid`? (set user identity)
- It's similar to `sudo` and used to run commands with elevated privileges.

```
setuid
What is it?
A special permission bit on executable files in Unix/Linux systems.
How does it work?
When a setuid program is run, it executes with the privileges of the file’s owner (often root or another user), not the user who launched it.
How is it set?
With chmod u+s filename (the s in the permissions, e.g., -rwsr-xr-x).
Example:
The passwd command is setuid root, so any user can change their password (which requires writing to /etc/shadow).
Security:
Can be risky if the program is not carefully written, as it can be exploited to gain unauthorized access.

sudo
What is it?
A command that allows permitted users to run specific commands as another user (usually root), as defined in the /etc/sudoers file.
How does it work?
You type sudo <command>, and if you’re authorized, the command runs with elevated privileges (often after you enter your password).
How is it configured?
By system administrators in the /etc/sudoers file, which controls who can run what as whom.
Example:
sudo apt update runs the update command as root.
Security:
More flexible and auditable than setuid. Logs usage, can restrict commands, and can require authentication.
Are they related?
Both allow running commands with different privileges than the current user.
setuid is a file permission mechanism; sudo is a program and a policy system.
sudo does not use setuid on the target command; instead, the sudo binary itself is setuid root, and it manages privilege escalation internally.
```

```bash
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ pwd
/home/bandit19
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ file ./bandit20-do 
./bandit20-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=35d353cf6d732f515a73f50ed205265fe1e68f90, for GNU/Linux 3.2.0, not stripped
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do euid=11020 cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

## 21
https://overthewire.org/wargames/bandit/bandit21.html
```
Level Goal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

Commands you may need to solve this level
ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)
```

```bash
bandit20@bandit:~$ echo -n "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 12345 &
[1] 3451427
bandit20@bandit:~$ ./suconnect 12345
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
[1]+  Done                    echo -n "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 12345
```
- https://mayadevbe.me/posts/overthewire/bandit/level21/

## 22
https://overthewire.org/wargames/bandit/bandit22.html
```
Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)
```

https://mayadevbe.me/posts/overthewire/bandit/level22/

Look at `/etc/cron.d` for what is running
`cat` /usr/bin/cronjob_bandit22.sh
...

I'll flesh this out tomorrow. My brain is dead.
It's tomorrow brain is still dead and it is 11:36 PM. Oof.

```
bandit21@bandit:~$ ls /etc/cron.d
clean_tmp  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  e2scrub_all  otw-tmp-dir  sysstat
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

## 23
https://overthewire.org/wargames/bandit/bandit23.html
```
Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)
```

```bash
bandit22@bandit:~$ ls /etc/cron.d
clean_tmp  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  e2scrub_all  otw-tmp-dir  sysstat
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ whoami
bandit22
bandit22@bandit:~$ myname=bandit23
bandit22@bandit:~$ echo I am user $myname | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```

## 24
https://overthewire.org/wargames/bandit/bandit24.html
```
Level Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

Commands you may need to solve this level
chmod, cron, crontab, crontab(5) (use “man 5 crontab” to access this)
```
https://mayadevbe.me/posts/overthewire/bandit/level24/
https://gist.github.com/achao-io/9155271f13f327e107a3b7b4d52c9e21

## 25
https://overthewire.org/wargames/bandit/bandit25.html
```
Level Goal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time
```

```bash
#!/bin/bash

bandit24_pass="gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"

# Generate all possibilities
for i in {0000..9999}; do
        echo "$bandit24_pass $i" >> possibilities.txt
done

# Pipe into nc
cat possibilities.txt | nc localhost 30002 | grep -A 1 "Correct"
```

```bash
bandit24@bandit:/tmp/tmp.fxamfep9s8$ ./crack.sh 
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```

## 26
https://overthewire.org/wargames/bandit/bandit26.html
```
Level Goal
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

Commands you may need to solve this level
ssh, cat, more, vi, ls, id, pwd
```
https://www.youtube.com/watch?v=CS7dKwFjQ58&ab_channel=CodeWithT

Holy, this one was crazy.

`cat /etc/passwd | grep bandit26`
`more`
`exec`
`export`
`make screen tiny`
`ssh -i`
`v`
`:e /etc/bandit_pass/bandit26`
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ

## 27
https://overthewire.org/wargames/bandit/bandit27.html
```
Level Goal
Good job getting a shell! Now hurry and grab the password for bandit27!

Commands you may need to solve this level
ls
```
```
make window tiny, to trigger `more`
ssh bandit.labs.overthewire.org -l bandit26 -p 2220
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
v
:set shell=/bin/bash
:shell (you can access a shell inside Vim!)
ls
./bandit27-do cat /etc/bandit_pass/bandit27
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```

## 28
https://overthewire.org/wargames/bandit/bandit28.html
```
Level Goal
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.

Commands you may need to solve this level
git
```
```bash
bandit27@bandit:~$ cd /tmp/tmp.eSXvL0jJFp
bandit27@bandit:/tmp/tmp.eSXvL0jJFp$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server on port 22, which is not intended.

bandit27-git@localhost: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
bandit27@bandit:/tmp/tmp.eSXvL0jJFp$ ls
bandit27@bandit:/tmp/tmp.eSXvL0jJFp$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
Permission denied, please try again.
bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
Receiving objects: 100% (3/3), 288 bytes | 288.00 KiB/s, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
bandit27@bandit:/tmp/tmp.eSXvL0jJFp$ ls
repo
bandit27@bandit:/tmp/tmp.eSXvL0jJFp$ cd repo
bandit27@bandit:/tmp/tmp.eSXvL0jJFp/repo$ ls -lh
total 4.0K
-rw-rw-r-- 1 bandit27 bandit27 68 May 16 22:22 README
bandit27@bandit:/tmp/tmp.eSXvL0jJFp/repo$ cat README 
The password to the next level is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

## 29
https://overthewire.org/wargames/bandit/bandit29.html
```
Level Goal
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

Commands you may need to solve this level
git
```
```bash
bandit28@bandit:~$ mktemp -d
/tmp/tmp.xHLs5ADHH7
bandit28@bandit:~$ cd /tmp/tmp.xHLs5ADHH7
bandit28@bandit:/tmp/tmp.xHLs5ADHH7$ ls
bandit28@bandit:/tmp/tmp.xHLs5ADHH7$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.xHLs5ADHH7$ ls
repo
bandit28@bandit:/tmp/tmp.xHLs5ADHH7$ cd repo
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ file README.md 
README.md: ASCII text
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ ls -lh
total 4.0K
-rw-rw-r-- 1 bandit28 bandit28 111 May 16 22:26 README.md
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ git history README.md
git: 'history' is not a git command. See 'git --help'.
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ git log
commit 674690a00a0056ab96048f7317b9ec20c057c06b (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    fix info leak

commit fb0df1358b1ff146f581651a84bae622353a71c0
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    add missing data

commit a5fdc97aae2c6f0e6c1e722877a100f24bcaaa46
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    initial commit of README.md

bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ git checkout fb0df1358b1ff146f581651a84bae622353a71c0
Note: switching to 'fb0df1358b1ff146f581651a84bae622353a71c0'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at fb0df13 add missing data
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

bandit28@bandit:/tmp/tmp.xHLs5ADHH7/repo$
```

## 30
https://overthewire.org/wargames/bandit/bandit30.html
```
Level Goal
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

Commands you may need to solve this level
git
```

```bash
% ssh bandit.labs.overthewire.org -l bandit29 -p 2220
bandit29@bandit:~$ mktemp -d
/tmp/tmp.7O5jQ2xRjR
bandit29@bandit:~$ cd /tmp/tmp.7O5jQ2xRjR
bandit29@bandit:/tmp/tmp.7O5jQ2xRjR$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
bandit29@bandit:/tmp/tmp.7O5jQ2xRjR/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.7O5jQ2xRjR/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev
bandit29@bandit:/tmp/tmp.7O5jQ2xRjR/repo$ git checkout dev
branch 'dev' set up to track 'origin/dev'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.7O5jQ2xRjR/repo$ git log
commit a97d0dbf8fd910ead6fcf648829ff55c1a629c8e (HEAD -> dev, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:21 2025 +0000

    add data needed for development

commit 3910630172946c9ffb75842922e394b772c672bd
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Apr 10 14:23:21 2025 +0000

    add gif2ascii

commit 3b8b91fc3c48f1a19d05670fd45d3e3f2621fcfa (origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Apr 10 14:23:21 2025 +0000

    fix username

commit 8d2ffeb5e45f87d0abb028aa796e3ebb63c5579c
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Apr 10 14:23:21 2025 +0000

    initial commit of README.md

bandit29@bandit:/tmp/tmp.7O5jQ2xRjR/repo$ git checkout a97d0dbf8fd910ead6fcf648829ff55c1a629c8e
Previous HEAD position was 3910630 add gif2ascii
HEAD is now at a97d0db add data needed for development
bandit29@bandit:/tmp/tmp.7O5jQ2xRjR/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
```

## 31
https://overthewire.org/wargames/bandit/bandit31.html
```
Level Goal
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

Commands you may need to solve this level
git
```

```bash
bandit30@bandit:~$ mktemp -d
/tmp/tmp.GRYqNuV23E
bandit30@bandit:~$ cd /tmp/tmp.GRYqNuV23E
bandit30@bandit:/tmp/tmp.GRYqNuV23E$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
bandit30@bandit:/tmp/tmp.GRYqNuV23E$ ls
repo
bandit30@bandit:/tmp/tmp.GRYqNuV23E$ cd repo
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ git tags
git: 'tags' is not a git command. See 'git --help'.

The most similar commands are
	stage
	tag
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ git checkout secret
fatal: reference is not a tree: secret
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ git tag secret
fatal: tag 'secret' already exists
bandit30@bandit:/tmp/tmp.GRYqNuV23E/repo$ git show secret
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```

## 32
https://overthewire.org/wargames/bandit/bandit32.html
```
Level Goal
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

Commands you may need to solve this level
git
```
```bash
bandit31@bandit:~$ mktemp -d
/tmp/tmp.JJtgE1h2R3
bandit31@bandit:~$ cd /tmp/tmp.JJtgE1h2R3
bandit31@bandit:/tmp/tmp.JJtgE1h2R3$ git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
bandit31@bandit:/tmp/tmp.JJtgE1h2R3$ ls
repo
bandit31@bandit:/tmp/tmp.JJtgE1h2R3$ cd repo
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ vim key.txt
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ gst
Command 'gst' not found, but there are 25 similar ones.
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ ls
key.txt  README.md
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ git add key.txt 
The following paths are ignored by one of your .gitignore files:
key.txt
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ git add -f key.txt 
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ git commit -m "May I come in?"
[master ed22139] May I come in?
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.JJtgE1h2R3/repo$ git push
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Permission denied, please try again.
bandit31-git@localhost's password: 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 327 bytes | 54.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
```

## 33
https://overthewire.org/wargames/bandit/bandit33.html
```
Level Goal
After all this git stuff, it’s time for another escape. Good luck!

Commands you may need to solve this level
sh, man
```
Key is to realize you can spawn a new shell by typing `$0`
```bash
$ $0
$ cat /etc/bandit_pass/bandit33
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```
