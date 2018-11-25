# Reading Files

## grep
Searches plain-text documents using a regular expression and returns matching lines. Originally part of a command called 'ed'. grep stands for 'globally search regular expression'

[Different use cases and switches for grep](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/)

### Flags

`-i` Case insensitive

`-o` Only matching: prints only the matched parts of a line

`-P` Interperts as a PERL regular expression (good for more advanced regex commands)

### Examples
Search the yum log for the word 'amazon'. The -i switch will search case insensitively

`cat /var/log/yum.log | grep -i "amazon"`

`grep -i "amazon" /var/log/yum.log` # grep can also take the path as an argument instead of being piped in

Search the yum log add return additional lines surrounding the match

`cat /var/log/yum.log | grep -i "amazon -C 3"` # context of three lines (3 lines before, 3 lines after)

`cat /var/log/yum.log | grep -i "amazon -B 4"` # prints 4 lines before the hit

`cat /var/log/yum.log | grep -i "amazon -A 4"` # prints 4 of lines after the hit

## rm
Remove files and directories from the file system

### Examples

`rm ./testfile.py` # deletes the file testfile.py

`rm -r ./testDirectory` # delete the directory (r flag means recursive)

## Links
[On the differences between less vs tail](https://www.brianstorti.com/stop-using-tail/)

## chown

Change owner of a file or directory

takes the parameters \[user id (uid)\]:\[group id (gid)\] to set permissions on specific users/groups

### Examples
``chown testUser /dir` changes the owner of the directory to testUser

`chown -R testUser:testGroup /dir` change the user owner to testUser and the group owner to testGroup and all subfiles and directories (-R recursively sets permissions)

`chown :testGroup /dir` change the group owner to testGroup
