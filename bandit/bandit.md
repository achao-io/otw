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
