# awk

## Usage
awk takes input from a program or file and processes the input line by line. It also accepts a pattern (regex or literal string) which it will try to match on each line and if it returns true it will execute an action inside of brackets. 

`awk '[pattern] {[action]}'`
pattern = a regular expression or a literal string to match
action = what to do with matched pattern

Both pattern and actions are optional, but one must be included.
If pattern is not provided, all lines are processed by the action
If action is not provided, all lines that match the pattern are printed
## Examples
### 

## Notes
### Splitting files and records
A record is created for each new line character. This can be overridden using the built-in RS variable.

`RS=","` = overrides the delimeter to a comma

As the input is processed, it can be accessed by using `$#`:

`$0` = Returns the entire string. Refered to as the **record**

`$1, $2, $3...` = index of separated values by white space

## Links
- https://www.tutorialspoint.com/awk/awk_basic_examples.htm
- [awk usages + manual](http://www.gnu.org/software/gawk/manual/gawk.html)
