## ps
Displays information about system processes

## pidof
Returns the process ID of a named process

### Examples
#### Return process id of 'bash' 
Will return multiple process ids of named process
```bash
pidof bash
```
```powershell
Get-Process bash | Select-Object -ExpandProperty ID 
```

#### Return first process id of 'bash' 
Will only return first process id of named process
```bash
pidof bash -s
```
```powershell
Get-Process bash | Select-Object -First 1 -ExpandProperty Id
```

## Links
- https://www.cyberciti.biz/faq/show-all-running-processes-in-linux/