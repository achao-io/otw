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
you need to know `strings` and `ltrace` to be able to solve this one.

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



