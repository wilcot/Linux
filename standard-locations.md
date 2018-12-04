| File Type | Linux Location | Windows Location |
| --------- | -------------- | ---------------- |
| System Logs | `/var/log` (access with dmesg or file parsing utility) | `system32\winevt\logs` (access via Event Viewer) |
| Tools and Optional Packages | `/opts` | `c:\program files` (? - no real equivalent) |
| User database | `/etc/passwd` | |
| System Configuration Directory | `/etc` | Windows Registry |
| disk management | `/etc/fstab` (file system table) | Disk Management |
| User Directory | `/home/[username]` | `c:\users\[username]` |
| Miscelaneous files (?) | `/var` (contains logs, cache and other dirs) |  |
| devices | (`/dev` |
| bash configuration | `~/.bashrc` and `etc/profile`| |
| system limits configuration | `/cat/security/limits.conf` | |


[Linux spec on directories](http://www.linuxbase.org/betaspecs/fhs/fhs/index.html)