## Standard Commands
| Linux Command | PowerShell Equivalent | CMD Equivalent | Description |
| ---- | ---- | ---- | ---- |
| [ps](./processes.md#ps), [pidof](./processes.md#pidof), [pgrep](./processes.md#pgrep) | Get-Process | tasklist | Get information about processes | Process Info |
| kill, killall, pkill | Stop-Process | taskkill |  Terminates a Process |
| grep | Select-String | FINDSTR | Search a file or piped output for regex matches. Returns lines that match |
| [awk](./awk.md) | A mixture of the following commands: `Get-Content, Select-String, Foreach-Object` | | Processes input from an app or file and processes text |
| sed | | | Edits a streat of text |
| curl | Invoke-WebRequest | | |
| less, tail | Get-Content -Tail | | Gets the last portions of a file |
| head | Get-Content -TotalCount | | Gets the first portions of a file |
| cat | `Get-Content` (to read files) OR `Add-Content` (to join files) | | Cat stands for concatenate and is officially used to join files. But it is typically used to output a short file |
| service, systemctl | | | |
| uname | | | Gets information about the kernel / system |
| dmesg | Get-EventLog (No PSCore support) | | Read system log messages |
| pwd | (Get-Location).Path | cd | Get the current working directory |
| [ls](./ls.md) | Get-ChildItem | dir | Get a listing of a directory |
| rm | Remove-Item | del | Remove an item from the file system |
| wc | Get-Content \| Measure-Object | <!-- no clue --> | Counts words and lines.. why?? |
| tee | Out-File | <!-- Not certain --> | Split contents of pipe to a file. Can write to both the terminal display and files |
| type | (Get-Command).Definition | which | Shows information about a command (built in or exec location) |
| xargs | Invoke-Expression | | Allows a command to be processed from the previous output or pipe |

## User and Groups Commands

| Linux Command | PowerShell Equivalent | CMD Equivalent | Description |
| ---- | ---- | ---- | ---- |
| useradd, adduser | New-LocalUser (No Linux Support) | net user [username] [password] /add | Add a local user |
| userdel | Remove-LocalUser (No Linux Support ) | net user [username] /delete | Remove a local user |
| gentent passwd | Get-LocalUser | | Look up local user | 
| passwd | | | change a password for a user |
| gpasswd | | | change a password for a group |

## File Management Commands

| Linux Command | PowerShell Equivalent | CMD Equivalent | Description |
| ---- | ---- | ---- | ---- |
| mkfs | Format-Volume | diskpart | Format / create a file system |
| wipefs | Format-Volume | diskpart | Clear file system |
| mount | | | Mount file device |
| umount | | | Un mount device |
| lsblk | | | Lists all block devices |
| chown | Set-Acl (No PSCore support) | | Change the owner of a file or folder |
| chmod | Set-Acl (No PSCore support) | | Change the permissions of a file or folder |


## Tips
- Type `Ctrl+R` in terminal to search the command history. Terminate the search with `Ctrl+G`
- To escape a frozen ssh session: Press the follow keys in order: Enter (Return key), ~ (tilda), . (period) 
