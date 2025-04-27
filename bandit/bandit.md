# bandit

## 0
- https://overthewire.org/wargames/bandit/bandit0.html
- `ssh <url> --login/-l <user> --port/-p XXXX`
- `ssh bandit.labs.overthewire.org -l bandit0 -p 2220`


## 0 -> 1
- https://overthewire.org/wargames/bandit/bandit1.html
- `ssh bandit.labs.overthewire.org -l bandit1 -p 2220`
- ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

## 1 -> 2
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


