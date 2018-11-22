# Examples
Things I know how to do on Windows that I want to accomplish on Linux

## Foreach-Object type commands

 #### Stop a single EC2 instance.
 
This works because the back ticks execute the AWS command to lookup an EC2 instance and jq parses the JSON to return an InstanceId. The -r in jq will strip out the double quotes.

``aws ec2 stop-instances --instance-ids `aws ec2 describe-instances | jq -r '.Reservations[0].Instances[0].InstanceId'` ``

 #### Stop all ec2 instances (more of a jq change)
``aws ec2 stop-instances --instance-ids `aws ec2 describe-instances | jq -r '.Reservations[].Instances[].InstanceId'` ``

## File Management

#### Copy a directory to a location and create a sym link 

The `mv` command does not support moving non-empty directories, so the easiest way was to use rsync to copy the entire directory to a new location, use rm to remove the files, then ln to create a symbolic link

```bash
rsync -a ~/Software/GitHub ~/Documents/GitHub   # -a creates an archive which copies permissions
rm -rf ~/Software/Github.   # -rf recursively deletes files and forces the deletion
ln -s ~/Documents/GitHub ~/Software/Github    # -s creates a symbolic link (instead of a hard link)
```

#### Format a volume and mount

Let's pretend we just created a new EBS volume and attached it to our instance via AWS console/cli. How do we find device (/dev/nvme1n1), format, and mount?

```bash
## Find device
ls /dev # should list all devies (and volumes) available to our system.. but that's a lot
ls -nap /dev | grep -i "^b" # we can also identify all deivices that art types of 'block'
lsblk -f # but the prettiest way is to use the lsblk command

## Format device
sudo mkfs -t xfs /dev/nvme1n1 # format to xfs file system
sudo mkdir /files # linux requires a directory to mount a file system to. So, lets create a files directory that we can mount ebs volume
sudo mount /dev/nvme1n1 /files # mount the files directory
```

#### Identify files with a certain string
grep can scan an entire directory and return matched files and the hits. Lets find all unit-files that have more than 2 occurrences of network

full command: `grep -R 'network' /lib/systemd/system | grep -oP '^(\/.+)(?=:(#| |\w))' | uniq -c | awk '$1>2 {print $2}'`

`grep -R 'network' /lib/systemd/system` Find all instances of the word 'network' under lib/systemd/system. R flag will recurrsively search the directory

**Note:** If we don't need the count, we could have accomplished this by just using the l flag on grep which will just return the list of unique files `grep -lR 'network' /lib/systemd/system`

This outputs something like this:
```bash
/lib/systemd/system/rpc-statd.service:Wants=network-online.target
/lib/systemd/system/rpc-statd.service:After=network-online.target nss-lookup.target rpcbind.socket
/lib/systemd/system/cloud-config.service:After=network-online.target cloud-config.target
/lib/systemd/system/cloud-config.service:Wants=network-online.target cloud-config.target
```

Lets grab just the file names
`grep -oP '^(\/.+)(?=:(#| |\w))'` The o flag will return only the matched portion of the string, and the P will use the perl regex engine. The pattern is looking for everything up to the first colon.

Now lets count the unique file names:
`uniq -c` -C will return the count. Output:

```
      3 /lib/systemd/system/cloud-init.service
      2 /lib/systemd/system/cloud-final.service
      1 /lib/systemd/system/update-motd.service
      1 /lib/systemd/system/amazon-ssm-agent.service
      2 /lib/systemd/system/chrony-dnssrv@.service
      2 /lib/systemd/system/nfs-lock.service
```

And finally filter it through awk
`awk '$1>2 {print $2}'` Compares the first column (count) to see if it's greater than 2, and prints the second column (file name) if it's true 
