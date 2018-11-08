| Linux Command | PowerShell Equivalent | CMD Equivalent | Description |
| ---- | ---- | ---- | ---- |
| [ps](./processes.md#ps), [pidof](./processes.md#pidof), [pgrep](./processes.md#pgrep) | Get-Process | tasklist | Get information about processes | Process Info |
| kill, killall, pkill | Stop-Process | taskkill |  Terminates a Process |
| grep | Select-String | FINDSTR | Search a file or piped output for regex matches. Returns lines that match |
| [awk](./awk.md) | A mixture of the following commands: Get-Content, Select-String, Foreach-Object | | Processes input from an app or file and processes text |
| sed | | | |
| curl | Invoke-WebRequest | | |
| tail | Get-Content -Tail | | Gets the last portions of a file |
| head | Get-Content -TotalCount | | Gets the first portions of a file |
| less | | | |
| cat | Get-Content | | Get entire contents of file |
| service, systemctl | | | |
| dmesg | | | Read system log messages |
