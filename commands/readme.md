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
| cat | Get-Content | | Get entire contents of file |
| service, systemctl | | | |
| dmesg | Get-EventLog (No PSCore support) | | Read system log messages |
| chown | Set-Acl (No PSCore support) | | Change the owner of a file or folder |
| chmod | Set-Acl (No PSCore support) | | Change the permissions of a file or folder |
| pwd | (Get-Location).Path | cd | Get the current working directory |

## User and Groups

| Linux Command | PowerShell Equivalent | CMD Equivalent | Description |
| useradd, adduser | New-LocalUser (No Linux Support) | net user [username] [password] /add | Add a local user |
| gentent passwd| Get-LocalUser | | Look up local user | 
