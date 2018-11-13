# File systems

Some Linux systems use EXT4/3 (Ubuntu, Debian) while others use XFS (RHEL, OpenSuse), and a new file system btrfs is being developed from scratch. The ext seems to be the tried and true file system for Linux

| File System | Description | Pros | Cons |
| ext3 | Third 'extended file system', introduced 2001. Main feature is journaling. Considered very stable.  | | |
| ext4 | Fourth 'extended file system', indtroduced 2008. Faster and more files than ext3. It seems like this has recently been considered stable enough for prod in the past few years | | |
| xfs | High performance file system | High parallel I/O and large file stores - used by NASA (damn!) | Slow deletes |
| btrfs | Pronounced 'better FS' or b-tree FS. Designed by Oracle and allows for copy-on-write | Allows for snapshots and checksums of files | |
| zfs | Developed by Sun. File system and Logical Volume Manager | Used for very large file systems | |

## Links
[Good Comparison of fs](https://www.unixmen.com/review-ext4-vs-btrfs-vs-xfs/)
[Another good comparison of even more FS](https://www.serverfocus.org/reiserfs-vs-ext4-vs-xfs-vs-zfs-vs-btrfs)