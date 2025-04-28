# bandit

## 0
- https://overthewire.org/wargames/bandit/bandit0.html
- `ssh <url> --login/-l <user> --port/-p XXXX`
- `ssh bandit.labs.overthewire.org -l bandit0 -p 2220`


## 1
- https://overthewire.org/wargames/bandit/bandit1.html
- `ssh bandit.labs.overthewire.org -l bandit1 -p 2220`
- ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## 2
- https://overthewire.org/wargames/bandit/bandit2.html
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
- https://overthewire.org/wargames/bandit/bandit3.html
- `more ~/"spaces in this filename"`
- MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## 4
- https://overthewire.org/wargames/bandit/bandit4.html
- The password for the next level is stored in a hidden file in the inhere directory.
```
% ls
% cd inhere
% ls -alh
% cat ...Hiding-From-You
```
- 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## 5
- https://overthewire.org/wargames/bandit/bandit5.html
- The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.
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
- https://overthewire.org/wargames/bandit/bandit6.html
- The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
human-readable
1033 bytes in size
not executable
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
