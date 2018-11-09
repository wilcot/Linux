# Reading Files

## grep
Searches plain-text documents using a regular expression and returns matching lines. Originally part of a command called 'ed'. grep stands for 'globally search regular expression'

[Different use cases and switches for grep](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/)

### Examples
Search the yum log for the word 'amazon'. The -i switch will search case insensitively
`cat /var/log/yum.log | grep -i "amazon"`

## Links
[On the differences between less vs tail](https://www.brianstorti.com/stop-using-tail/)