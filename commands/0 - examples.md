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
