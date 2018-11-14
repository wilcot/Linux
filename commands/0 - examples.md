# Examples
Things I know how to do on Windows that I want to accomplish on Linux

## Foreach-Object type commands

 ### Stops a single instance. This works because the back ticks execute the AWS command and jq processes the json query result. The -r in jq will strip out the double quotes 

``aws ec2 stop-instances --instance-ids `aws ec2 describe-instances | jq -r '.Reservations[0].Instances[0].InstanceId'` ``


