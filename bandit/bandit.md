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
```
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
```
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
```
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
```
% grep millionth data.txt 
millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

## 9
https://overthewire.org/wargames/bandit/bandit9.html
```
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once
```
- tried `cat data.txt | uniq -u` first, but didn't work. This is because `uniq` only removes consecutive duplicate lines. If duplicate lines are not adjacent, `uniq` won't consider them duplicates. To make sure identical lines are next to each other, `sort` the file first.
```
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

```
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
```
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
```
% cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

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

```
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
```
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ xxd -r data.txt 
4 4��hH��D0UP�k�.�"˟�����D�p�QG�l��J��΄�x Fc������޺�����߰;���4�
��px��[�h���oFw9 D���9A���\Ѽ-�1�l�N�(^�@Z@T!��I2_=pi@�����(,Q�I��/bݐ'�y��R�
                                                                           ���t�����2Z������<wm�i�<G�f�K���j    F��]    �pk��%��

��Zip�47��@��X\5�<�ڟQ��զ��G�8�P�����B�eI@
�����P�YK?+�� ��$��N��%Φ�g�Nm!A6*�)-f8<!��N��O,���6Ɉ�V8�w$S�
```

now to uncompress... gzip? bzip2? tar? checking man pages

```
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

```
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ file output.bin
output.bin: gzip compressed data, was "data2.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 585
```

so gzip

```
bandit12@bandit:/tmp/tmp.MbsFdVhoZU$ gzip -d output.bin
gzip: output.bin: unknown suffix -- ignored
```

problem is, gzip is expecting a file ending with `.gz`. so, use `-f` or add the `.gz` extension

``
wow, that was like 8 layers deep of `gzip -d`, `bzip2 -d`, `tar xvf`. Each step using `file` to understand what compression was used. Make sure file extension for `gzip` ends in `gz` and `bzip2` ends in `bz2`.

here is the work: https://gist.github.com/achao-io/4e14b332f67d80a12a612e6329d0bb1f

```
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

```
bandit13@bandit:~$ ssh bandit.labs.overthewire.org -l bandit14 -p 2220 -i sshkey.private
```