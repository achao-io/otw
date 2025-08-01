# leviathan
https://overthewire.org/wargames/leviathan/

```
Dare you face the lord of the oceans?
Leviathan is a wargame that has been rescued from the demise of intruded.net, previously hosted on leviathan.intruded.net. Big thanks to adc, morla and reth for their help in resurrecting this game!

What follows below is the original description of leviathan, copied from intruded.net:

Summary:
Difficulty:     1/10
Levels:         8
Platform:   Linux/x86

Author:
Anders Tonfeldt

Special Thanks:
We would like to thank AstroMonk for coming up with a replacement idea for the last level,
deadfood for finding a leveljump and Coi for finding a non-planned vulnerability.

Description:
This wargame doesn't require any knowledge about programming - just a bit of common
sense and some knowledge about basic *nix commands. We had no idea that it'd be this
hard to make an interesting wargame that wouldn't require programming abilities from 
the players. Hopefully we made an interesting challenge for the new ones.
Leviathan’s levels are called leviathan0, leviathan1, … etc. and can be accessed on leviathan.labs.overthewire.org through SSH on port 2223.

To login to the first level use:

Username: leviathan0
Password: leviathan0
Data for the levels can be found in the homedirectories. You can look at /etc/leviathan_pass for the various level passwords.
```

## 0->1
This level involves `grep`-ing a directory.

```bash
% ssh leviathan.labs.overthewire.org -l leviathan0 -p 2223

leviathan0@gibson:~$ ls -alh
total 24K
drwxr-xr-x  3 root       root       4.0K Apr 10 14:23 .
drwxr-xr-x 83 root       root       4.0K Apr 10 14:24 ..
drwxr-x---  2 leviathan1 leviathan0 4.0K Apr 10 14:23 .backup
-rw-r--r--  1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root       root       3.7K Mar 31  2024 .bashrc
-rw-r--r--  1 root       root        807 Mar 31  2024 .profile
leviathan0@gibson:~$ cd .backup/
leviathan0@gibson:~/.backup$ ls -lh
total 132K
-rw-r----- 1 leviathan1 leviathan0 131K Apr 10 14:23 bookmarks.html
leviathan0@gibson:~/.backup$ grep leviathan bookmarks.html 
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is 3QJ3TgzHDq" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

## 1->2
This level introduces us to two commands, ltrace and strings.


```bash
% ssh leviathan.labs.overthewire.org -l leviathan1 -p 2223
leviathan1@gibson:~$ ls -lh
total 16K
-r-sr-x--- 1 leviathan2 leviathan1 15K Apr 10 14:23 check
leviathan1@gibson:~$ file check
check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=990fa9b7d511205601669835610d587780d0195e, for GNU/Linux 3.2.0, not stripped
leviathan1@gibson:~$ whoami
leviathan1
leviathan1@gibson:~$ ./check
password: test
Wrong password, Good Bye ...
leviathan1@gibson:~$ ltrace ./check
__libc_start_main(0x80490ed, 1, 0xffffd494, 0 <unfinished ...>
printf("password: ")                                                                = 10
getchar(0, 0, 0x786573, 0x646f67password: test
)                                                   = 116
getchar(0, 116, 0x786573, 0x646f67)                                                 = 101
getchar(0, 0x6574, 0x786573, 0x646f67)                                              = 115
strcmp("tes", "sex")                                                                = 1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                = 29
+++ exited (status 0) +++
leviathan1@gibson:~$ ./check
password: sex
$ whoami
leviathan2
$ cat /etc/leviathan_pass/leviathan2
NsN1HwFoyN
```


## 2->3
This level involves creating a symbolic link (symlink) which enables privilege escalation by exploiting how the printfile binary handles file inputs.

By creating a symlink and calling the printfile binary with a filename that includes a space, you leverage the improper input handling in the program. This combination allows access to files that leviathan2 wouldn’t normally have permissions for, thus effectively "hacking" the system to print the sensitive file's contents.

Feeding two inputs to the printfile binary gives us several insights into how the binary processes inputs and how it manages to retrieve file contents. The behavior of the binary with two inputs shows that it accepts and processes only the first argument. The first step in the binary’s execution is to perform an access check for the first file. The `snprintf` call shows how the command is constructed. The calls to `geteuid()` reveal the effective user ID during execution. By running `ltrace`, you can infer potential vulnerabilities.

The fact that input parsing only considers the first file suggests that if unexpected input patterns (like filenames with spaces) are used, it might exploit the way the binary interprets or constructs file names. This detail can lead to privilege escalation tactics.


```bash
% ssh leviathan.labs.overthewire.org -l leviathan2 -p 2223

leviathan2@gibson:~$ ls -alh
total 36K
drwxr-xr-x  2 root       root       4.0K Apr 10 14:23 .
drwxr-xr-x 83 root       root       4.0K Apr 10 14:24 ..
-rw-r--r--  1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root       root       3.7K Mar 31  2024 .bashrc
-r-sr-x---  1 leviathan3 leviathan2  15K Apr 10 14:23 printfile
-rw-r--r--  1 root       root        807 Mar 31  2024 .profile
leviathan2@gibson:~$ file printfile 
printfile: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=79cfa8b87bb611f9cf6d6865010709e2ba5c8e3f, for GNU/Linux 3.2.0, not stripped
leviathan2@gibson:~$ ./printfile 
*** File Printer ***
Usage: ./printfile filename
leviathan2@gibson:~$ ./printfile .bash_logout 
# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
leviathan2@gibson:~$ ./printfile .bash_logout .profile
# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
leviathan2@gibson:~$ ltrace ./printfile .bash_logout .profile
__libc_start_main(0x80490ed, 3, 0xffffd464, 0 <unfinished ...>
access(".bash_logout", 4)                                                           = 0
snprintf("/bin/cat .bash_logout", 511, "/bin/cat %s", ".bash_logout")               = 21
geteuid()                                                                           = 12002
geteuid()                                                                           = 12002
setreuid(12002, 12002)                                                              = 0
system("/bin/cat .bash_logout"# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                              = 0
+++ exited (status 0) +++
leviathan2@gibson:~$ mktemp -d
/tmp/tmp.kDdtlswch4
leviathan2@gibson:~$ cd /tmp/tmp.kDdtlswch4
leviathan2@gibson:/tmp/tmp.kDdtlswch4$ touch "test file.txt"
leviathan2@gibson:/tmp/tmp.kDdtlswch4$ cd ~
leviathan2@gibson:~$ ./printfile /tmp/tmp.kDdtlswch4/test\ file.txt 
/bin/cat: /tmp/tmp.kDdtlswch4/test: Permission denied
/bin/cat: file.txt: No such file or directory
leviathan2@gibson:~$ ./printfile /tmp/tmp.kDdtlswch4/"test file.txt"
/bin/cat: /tmp/tmp.kDdtlswch4/test: Permission denied
/bin/cat: file.txt: No such file or directory
leviathan2@gibson:~$ ltrace ./printfile /tmp/tmp.kDdtlswch4/"test file.txt"
__libc_start_main(0x80490ed, 2, 0xffffd434, 0 <unfinished ...>
access("/tmp/tmp.kDdtlswch4/test file.tx"..., 4)                                    = 0
snprintf("/bin/cat /tmp/tmp.kDdtlswch4/tes"..., 511, "/bin/cat %s", "/tmp/tmp.kDdtlswch4/test file.tx"...) = 42
geteuid()                                                                           = 12002
geteuid()                                                                           = 12002
setreuid(12002, 12002)                                                              = 0
system("/bin/cat /tmp/tmp.kDdtlswch4/tes".../bin/cat: /tmp/tmp.kDdtlswch4/test: No such file or directory
/bin/cat: file.txt: No such file or directory
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                              = 256
+++ exited (status 0) +++
leviathan2@gibson:~$ cd /tmp/tmp.kDdtlswch4
leviathan2@gibson:/tmp/tmp.kDdtlswch4$ ln -s /etc/leviathan_pass/leviathan3 ./test
leviathan2@gibson:/tmp/tmp.kDdtlswch4$ ls -alh
total 232K
drwx------   2 leviathan2 leviathan2 4.0K May 24 02:25 .
drwxrwx-wt 559 root       root       224K May 24 02:25 ..
lrwxrwxrwx   1 leviathan2 leviathan2   30 May 24 02:25 test -> /etc/leviathan_pass/leviathan3
-rw-rw-r--   1 leviathan2 leviathan2    0 May 24 02:22 test file.txt
leviathan2@gibson:/tmp/tmp.kDdtlswch4$ cd ~
leviathan2@gibson:~$ ./printfile /tmp/tmp.kDdtlswch4/"test file.txt"
/bin/cat: /tmp/tmp.kDdtlswch4/test: Permission denied
/bin/cat: file.txt: No such file or directory
leviathan2@gibson:~$ chmod 777 /tmp/tmp.kDdtlswch4
leviathan2@gibson:~$ ./printfile /tmp/tmp.kDdtlswch4/"test file.txt"
f0n8h2iWLP
/bin/cat: file.txt: No such file or directory
```


## 3->4
This level involves using `ltrace`.

```bash
leviathan3@gibson:~$ ls -alh
total 40K
drwxr-xr-x  2 root       root       4.0K Apr 10 14:23 .
drwxr-xr-x 83 root       root       4.0K Apr 10 14:24 ..
-rw-r--r--  1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root       root       3.7K Mar 31  2024 .bashrc
-r-sr-x---  1 leviathan4 leviathan3  18K Apr 10 14:23 level3
-rw-r--r--  1 root       root        807 Mar 31  2024 .profile
leviathan3@gibson:~$ ./level3
Enter the password> test
bzzzzzzzzap. WRONG
leviathan3@gibson:~$ ltrace ./level3
__libc_start_main(0x80490ed, 1, 0xffffd494, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                                                          = -1
printf("Enter the password> ")                                                      = 20
fgets(Enter the password> test
"test\n", 256, 0xf7fae5c0)                                                    = 0xffffd26c
strcmp("test\n", "snlprintf\n")                                                     = 1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                                          = 19
+++ exited (status 0) +++
leviathan3@gibson:~$ ./level3 snlprintf
Enter the password> snlprintf
[You've got shell]!
$ whoami
leviathan4
$ cat /etc/leviathan_pass/leviathan4
WG1egElCvO
```


## 4->5
This level involves using `ltrace` and converting binary bits into bytes and reading those as UTF8.

https://mayadevbe.me/posts/overthewire/leviathan/level5/
>Binary code is the most basic representation of data for a computer. This is what the computer uses internally. It comes from the binary number system, which only includes ‘0’ and ‘1’ as digits, also called ‘bits’.

>In computer science, there are different encodings to represent human-readable text. The most basic and common one is the ‘American Standard Code for Information Interchange’ (ASCII). ASCII uses 7 bits to represent one character. Generally, if you were to transform binary to ASCII per hand, you would first transform binary to our decimal system and look up the corresponding letter in an ASCII table. Example: ‘01000001’ -> ‘65’ -> ‘A’.


```bash
leviathan4@gibson:~$ ls -lah
total 24K
drwxr-xr-x  3 root root       4.0K Apr 10 14:23 .
drwxr-xr-x 83 root root       4.0K Apr 10 14:24 ..
-rw-r--r--  1 root root        220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root root       3.7K Mar 31  2024 .bashrc
-rw-r--r--  1 root root        807 Mar 31  2024 .profile
dr-xr-x---  2 root leviathan4 4.0K Apr 10 14:23 .trash
leviathan4@gibson:~$ cd .trash
leviathan4@gibson:~/.trash$ ls -alh
total 24K
dr-xr-x--- 2 root       leviathan4 4.0K Apr 10 14:23 .
drwxr-xr-x 3 root       root       4.0K Apr 10 14:23 ..
-r-sr-x--- 1 leviathan5 leviathan4  15K Apr 10 14:23 bin
leviathan4@gibson:~/.trash$ file bin
bin: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=52e379ac2e364243895250cb84038a8bf5d3e4e5, for GNU/Linux 3.2.0, not stripped
leviathan4@gibson:~/.trash$ ./bin
00110000 01100100 01111001 01111000 01010100 00110111 01000110 00110100 01010001 01000100 00001010 
leviathan4@gibson:~/.trash$ ltrace ./bin
__libc_start_main(0x80490ad, 1, 0xffffd464, 0 <unfinished ...>
fopen("/etc/leviathan_pass/leviathan5", "r")                                       = 0
+++ exited (status 255) +++
leviathan4@gibson:~/.trash$ mktemp -d
/tmp/tmp.mS55LhfiAZ
leviathan4@gibson:~/.trash$ ./bin > /tmp/tmp.mS55LhfiAZ/bin.txt
leviathan4@gibson:~/.trash$ cd /tmp/tmp.mS55LhfiAZ
leviathan4@gibson:/tmp/tmp.mS55LhfiAZ$ ls
bin.txt
leviathan4@gibson:/tmp/tmp.mS55LhfiAZ$ cat bin.txt 
00110000 01100100 01111001 01111000 01010100 00110111 01000110 00110100 01010001 01000100 00001010
leviathan4@gibson:/tmp/tmp.mS55LhfiAZ$ python3 bin_convert.py 
0dyxT7F4QD
```

```python
with open("bin.txt") as f:
    data = f.read()

data = data.strip()
binary_bit_list = data.split(" ")
res = ""

for bits in binary_bit_list:
    res += chr(int(bits, 2))

print(res)
```


## 5->6
This level uses `ltrace` with `ln -s`.

```bash
leviathan5@gibson:~$ ls -alh
total 36K
drwxr-xr-x  2 root       root       4.0K Apr 10 14:23 .
drwxr-xr-x 83 root       root       4.0K Apr 10 14:24 ..
-rw-r--r--  1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root       root       3.7K Mar 31  2024 .bashrc
-r-sr-x---  1 leviathan6 leviathan5  15K Apr 10 14:23 leviathan5
-rw-r--r--  1 root       root        807 Mar 31  2024 .profile
leviathan5@gibson:~$ file leviathan5 
leviathan5: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=0fbe5a715bf8cd28d02bc0e989a37f9c0ab21614, for GNU/Linux 3.2.0, not stripped
leviathan5@gibson:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@gibson:~$ ltrace ./leviathan5 
__libc_start_main(0x804910d, 1, 0xffffd484, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                       = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)                                                 = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan5@gibson:~$ touch /tmp/file.log
leviathan5@gibson:~$ ltrace ./leviathan5 
__libc_start_main(0x804910d, 1, 0xffffd484, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                       = 0x804d1a0
fgetc(0x804d1a0)                                                                  = '\377'
feof(0x804d1a0)                                                                   = 1
fclose(0x804d1a0)                                                                 = 0
getuid()                                                                          = 12005
setuid(12005)                                                                     = 0
unlink("/tmp/file.log")                                                           = 0
+++ exited (status 0) +++
leviathan5@gibson:~$ echo "cat /etc/leviathan_pass/leviathan6" > /tmp/file.log
leviathan5@gibson:~$ ltrace ./leviathan5 
__libc_start_main(0x804910d, 1, 0xffffd484, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                       = 0x804d1a0
fgetc(0x804d1a0)                                                                  = 'c'
feof(0x804d1a0)                                                                   = 0
putchar(99, 0x804a008, 0, 0)                                                      = 99
fgetc(0x804d1a0)                                                                  = 'a'
feof(0x804d1a0)                                                                   = 0
putchar(97, 0x804a008, 0, 0)                                                      = 97
fgetc(0x804d1a0)                                                                  = 't'
feof(0x804d1a0)                                                                   = 0
putchar(116, 0x804a008, 0, 0)                                                     = 116
fgetc(0x804d1a0)                                                                  = ' '
feof(0x804d1a0)                                                                   = 0
putchar(32, 0x804a008, 0, 0)                                                      = 32
fgetc(0x804d1a0)                                                                  = '/'
feof(0x804d1a0)                                                                   = 0
putchar(47, 0x804a008, 0, 0)                                                      = 47
fgetc(0x804d1a0)                                                                  = 'e'
feof(0x804d1a0)                                                                   = 0
putchar(101, 0x804a008, 0, 0)                                                     = 101
fgetc(0x804d1a0)                                                                  = 't'
feof(0x804d1a0)                                                                   = 0
putchar(116, 0x804a008, 0, 0)                                                     = 116
fgetc(0x804d1a0)                                                                  = 'c'
feof(0x804d1a0)                                                                   = 0
putchar(99, 0x804a008, 0, 0)                                                      = 99
fgetc(0x804d1a0)                                                                  = '/'
feof(0x804d1a0)                                                                   = 0
putchar(47, 0x804a008, 0, 0)                                                      = 47
fgetc(0x804d1a0)                                                                  = 'l'
feof(0x804d1a0)                                                                   = 0
putchar(108, 0x804a008, 0, 0)                                                     = 108
fgetc(0x804d1a0)                                                                  = 'e'
feof(0x804d1a0)                                                                   = 0
putchar(101, 0x804a008, 0, 0)                                                     = 101
fgetc(0x804d1a0)                                                                  = 'v'
feof(0x804d1a0)                                                                   = 0
putchar(118, 0x804a008, 0, 0)                                                     = 118
fgetc(0x804d1a0)                                                                  = 'i'
feof(0x804d1a0)                                                                   = 0
putchar(105, 0x804a008, 0, 0)                                                     = 105
fgetc(0x804d1a0)                                                                  = 'a'
feof(0x804d1a0)                                                                   = 0
putchar(97, 0x804a008, 0, 0)                                                      = 97
fgetc(0x804d1a0)                                                                  = 't'
feof(0x804d1a0)                                                                   = 0
putchar(116, 0x804a008, 0, 0)                                                     = 116
fgetc(0x804d1a0)                                                                  = 'h'
feof(0x804d1a0)                                                                   = 0
putchar(104, 0x804a008, 0, 0)                                                     = 104
fgetc(0x804d1a0)                                                                  = 'a'
feof(0x804d1a0)                                                                   = 0
putchar(97, 0x804a008, 0, 0)                                                      = 97
fgetc(0x804d1a0)                                                                  = 'n'
feof(0x804d1a0)                                                                   = 0
putchar(110, 0x804a008, 0, 0)                                                     = 110
fgetc(0x804d1a0)                                                                  = '_'
feof(0x804d1a0)                                                                   = 0
putchar(95, 0x804a008, 0, 0)                                                      = 95
fgetc(0x804d1a0)                                                                  = 'p'
feof(0x804d1a0)                                                                   = 0
putchar(112, 0x804a008, 0, 0)                                                     = 112
fgetc(0x804d1a0)                                                                  = 'a'
feof(0x804d1a0)                                                                   = 0
putchar(97, 0x804a008, 0, 0)                                                      = 97
fgetc(0x804d1a0)                                                                  = 's'
feof(0x804d1a0)                                                                   = 0
putchar(115, 0x804a008, 0, 0)                                                     = 115
fgetc(0x804d1a0)                                                                  = 's'
feof(0x804d1a0)                                                                   = 0
putchar(115, 0x804a008, 0, 0)                                                     = 115
fgetc(0x804d1a0)                                                                  = '/'
feof(0x804d1a0)                                                                   = 0
putchar(47, 0x804a008, 0, 0)                                                      = 47
fgetc(0x804d1a0)                                                                  = 'l'
feof(0x804d1a0)                                                                   = 0
putchar(108, 0x804a008, 0, 0)                                                     = 108
fgetc(0x804d1a0)                                                                  = 'e'
feof(0x804d1a0)                                                                   = 0
putchar(101, 0x804a008, 0, 0)                                                     = 101
fgetc(0x804d1a0)                                                                  = 'v'
feof(0x804d1a0)                                                                   = 0
putchar(118, 0x804a008, 0, 0)                                                     = 118
fgetc(0x804d1a0)                                                                  = 'i'
feof(0x804d1a0)                                                                   = 0
putchar(105, 0x804a008, 0, 0)                                                     = 105
fgetc(0x804d1a0)                                                                  = 'a'
feof(0x804d1a0)                                                                   = 0
putchar(97, 0x804a008, 0, 0)                                                      = 97
fgetc(0x804d1a0)                                                                  = 't'
feof(0x804d1a0)                                                                   = 0
putchar(116, 0x804a008, 0, 0)                                                     = 116
fgetc(0x804d1a0)                                                                  = 'h'
feof(0x804d1a0)                                                                   = 0
putchar(104, 0x804a008, 0, 0)                                                     = 104
fgetc(0x804d1a0)                                                                  = 'a'
feof(0x804d1a0)                                                                   = 0
putchar(97, 0x804a008, 0, 0)                                                      = 97
fgetc(0x804d1a0)                                                                  = 'n'
feof(0x804d1a0)                                                                   = 0
putchar(110, 0x804a008, 0, 0)                                                     = 110
fgetc(0x804d1a0)                                                                  = '6'
feof(0x804d1a0)                                                                   = 0
putchar(54, 0x804a008, 0, 0)                                                      = 54
fgetc(0x804d1a0)                                                                  = '\n'
feof(0x804d1a0)                                                                   = 0
putchar(10, 0x804a008, 0, 0cat /etc/leviathan_pass/leviathan6
)                                                      = 10
fgetc(0x804d1a0)                                                                  = '\377'
feof(0x804d1a0)                                                                   = 1
fclose(0x804d1a0)                                                                 = 0
getuid()                                                                          = 12005
setuid(12005)                                                                     = 0
unlink("/tmp/file.log")                                                           = 0
+++ exited (status 0) +++
leviathan5@gibson:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@gibson:~$ ./leviathan5
szo7HDB88w
```

## 6->7
This one is crazy.

`gdb`, knowledge of Assembly, registers, `setreuid@plt`, 

Best to reference this.
https://mayadevbe.me/posts/overthewire/leviathan/level7/

```bash
leviathan6@gibson:~$ ./leviathan6 
usage: ./leviathan6 <4 digit code>
leviathan6@gibson:~$ ltrace ./leviathan6 000
__libc_start_main(0x80490dd, 2, 0xffffd474, 0 <unfinished ...>
atoi(0xffffd5e3, 0, 0, 0)                                                        = 0
puts("Wrong"Wrong
)                                                                    = 6
+++ exited (status 0) +++
leviathan6@gibson:~$ ltrace ./leviathan6 0001
__libc_start_main(0x80490dd, 2, 0xffffd474, 0 <unfinished ...>
atoi(0xffffd5e2, 0, 0, 0)                                                        = 1
puts("Wrong"Wrong
)                                                                    = 6
+++ exited (status 0) +++
leviathan6@gibson:~$ ltrace ./leviathan6 5555
__libc_start_main(0x80490dd, 2, 0xffffd474, 0 <unfinished ...>
atoi(0xffffd5e2, 0, 0, 0)                                                        = 5555
puts("Wrong"Wrong
)                                                                    = 6
+++ exited (status 0) +++
...
leviathan6@gibson:~$ gdb --args leviathan6 0000
GNU gdb (Ubuntu 15.0.50.20240403-0ubuntu1) 15.0.50.20240403-git
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from leviathan6...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /home/leviathan6/leviathan6.
(No debugging symbols found in leviathan6)
(gdb) disassemble main
Dump of assembler code for function main:
   0x080491c6 <+0>:	lea    0x4(%esp),%ecx
   0x080491ca <+4>:	and    $0xfffffff0,%esp
   0x080491cd <+7>:	push   -0x4(%ecx)
   0x080491d0 <+10>:	push   %ebp
   0x080491d1 <+11>:	mov    %esp,%ebp
   0x080491d3 <+13>:	push   %ebx
   0x080491d4 <+14>:	push   %ecx
   0x080491d5 <+15>:	sub    $0x10,%esp
   0x080491d8 <+18>:	mov    %ecx,%eax
   0x080491da <+20>:	movl   $0x1bd3,-0xc(%ebp)
   0x080491e1 <+27>:	cmpl   $0x2,(%eax)
   0x080491e4 <+30>:	je     0x8049206 <main+64>
   0x080491e6 <+32>:	mov    0x4(%eax),%eax
   0x080491e9 <+35>:	mov    (%eax),%eax
   0x080491eb <+37>:	sub    $0x8,%esp
   0x080491ee <+40>:	push   %eax
   0x080491ef <+41>:	push   $0x804a008
   0x080491f4 <+46>:	call   0x8049040 <printf@plt>
   0x080491f9 <+51>:	add    $0x10,%esp
   0x080491fc <+54>:	sub    $0xc,%esp
   0x080491ff <+57>:	push   $0xffffffff
   0x08049201 <+59>:	call   0x8049080 <exit@plt>
   0x08049206 <+64>:	mov    0x4(%eax),%eax
   0x08049209 <+67>:	add    $0x4,%eax
   0x0804920c <+70>:	mov    (%eax),%eax
   0x0804920e <+72>:	sub    $0xc,%esp
   0x08049211 <+75>:	push   %eax
   0x08049212 <+76>:	call   0x80490a0 <atoi@plt>
   0x08049217 <+81>:	add    $0x10,%esp
   0x0804921a <+84>:	cmp    %eax,-0xc(%ebp)
   0x0804921d <+87>:	jne    0x804924a <main+132>
   0x0804921f <+89>:	call   0x8049050 <geteuid@plt>
   0x08049224 <+94>:	mov    %eax,%ebx
   0x08049226 <+96>:	call   0x8049050 <geteuid@plt>
   0x0804922b <+101>:	sub    $0x8,%esp
   0x0804922e <+104>:	push   %ebx
   0x0804922f <+105>:	push   %eax
   0x08049230 <+106>:	call   0x8049090 <setreuid@plt>
   0x08049235 <+111>:	add    $0x10,%esp
   0x08049238 <+114>:	sub    $0xc,%esp
   0x0804923b <+117>:	push   $0x804a022
   0x08049240 <+122>:	call   0x8049070 <system@plt>
   0x08049245 <+127>:	add    $0x10,%esp
   0x08049248 <+130>:	jmp    0x804925a <main+148>
--Type <RET> for more, q to quit, c to continue without paging--c
   0x0804924a <+132>:	sub    $0xc,%esp
   0x0804924d <+135>:	push   $0x804a02a
   0x08049252 <+140>:	call   0x8049060 <puts@plt>
   0x08049257 <+145>:	add    $0x10,%esp
   0x0804925a <+148>:	mov    $0x0,%eax
   0x0804925f <+153>:	lea    -0x8(%ebp),%esp
   0x08049262 <+156>:	pop    %ecx
   0x08049263 <+157>:	pop    %ebx
   0x08049264 <+158>:	pop    %ebp
   0x08049265 <+159>:	lea    -0x4(%ecx),%esp
   0x08049268 <+162>:	ret
End of assembler dump.
(gdb) b *0x0804921a
Breakpoint 1 at 0x804921a
(gdb) run
Starting program: /home/leviathan6/leviathan6 0000
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804921a in main ()
(gdb) info registers
eax            0x0                 0
ecx            0xffffd5c7          -10809
edx            0x0                 0
ebx            0xf7fade34          -134554060
esp            0xffffd360          0xffffd360
ebp            0xffffd378          0xffffd378
esi            0xffffd450          -11184
edi            0xf7ffcb60          -134231200
eip            0x804921a           0x804921a <main+84>
eflags         0x286               [ PF SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
gs             0x63                99
k0             0x0                 0
k1             0x0                 0
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0
(gdb) print $ebp-0xc
$1 = (void *) 0xffffd36c
(gdb) x 0xffffd36c
0xffffd36c:	7123
(gdb) help x
Examine memory: x/FMT ADDRESS.
ADDRESS is an expression for the memory address to examine.
FMT is a repeat count followed by a format letter and a size letter.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),
  t(binary), f(float), a(address), i(instruction), c(char), s(string)
  and z(hex, zero padded on the left).
Size letters are b(byte), h(halfword), w(word), g(giant, 8 bytes).
The specified number of objects of the specified size are printed
according to the format.  If a negative number is specified, memory is
examined backward from the address.

Defaults for format and size letters are those previously used.
Default count is 1.  Default address is following last thing printed
with this command or "print".
(gdb) q
leviathan6@gibson:~$ ./leviathan6 7123
$ cat /etc/leviathan_pass/leviathan7
qEs5Io5yM8
...
leviathan7@gibson:~$ ls -alh
total 24K
drwxr-xr-x  2 root       root       4.0K Apr 10 14:23 .
drwxr-xr-x 83 root       root       4.0K Apr 10 14:24 ..
-rw-r--r--  1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--  1 root       root       3.7K Mar 31  2024 .bashrc
-r--r-----  1 leviathan7 leviathan7  178 Apr 10 14:23 CONGRATULATIONS
-rw-r--r--  1 root       root        807 Mar 31  2024 .profile
leviathan7@gibson:~$ cat CONGRATULATIONS 
Well Done, you seem to have used a *nix system before, now try something more serious.
(Please don't post writeups, solutions or spoilers about the games on the web. Thank you!)
```
