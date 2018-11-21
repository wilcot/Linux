# Volume Management

/dev directory contains all the devices that are available to the system. If a new volume or peripheral is attached to the instance, it will become available in this directory

/etc/fstab is a configuration file that contains information on how to mount volumes to the system

## fstab

This file contains a list of devices and where / how they should be mounted

### Columns

1 - The device that should be mounted. Either the location (/dev/sdf) or UUID (some guid)
2 - Where the device should be mounted to. This requires a folder to already be created
3 - File system type (ext4, xfs, etc)
4 - Option

### Example
UUID=4bb710f5-05c3-4e94-bfc9-4a9dcfe895e0 / xfs defaults,noatime 1  1

## lsblk

List Block devices - provides a nested view of block devices and their mounts

### Example

`lsblk -f` prints list of block devices, volumes and their file systems