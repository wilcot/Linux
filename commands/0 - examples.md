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
