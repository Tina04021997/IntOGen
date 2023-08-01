# IntOGen under AWS
## Using AWS EC2 instances
1. Login AWS account
2. Go to the top right corner, choose the *us-west-1* channel (US West (N.California))
3. Choose *EC2* console
4. Go to Images > AMIs
5. Select your idea instance (e.g., Phoebe-intogen-plus) and hit *launch instance from AMI*
6. Modify the following fields:
   - Name and tags
   - Instance type: e.g., c5-18xlarge
   - Key pair

## Running IntOGen in the instance
1. Create the intogen bash script `DCIS_new.sh` under intogen-plus folder
2. 

## Creating key pairs
1. Create an instance and at the Key pair section, create a new key
2. You will get a pem file, place it on your local desktop
3. On the terminal, do `chmod 400 Tina_intogen_2023.pem` to change the permission
4. Go back to your AWS instance and copy the *Public IPv4 DNS* Address
5. In your terminal, do `ssh -i Tina_intogen_2023.pem ubuntu@{IPv4 address}` (make sure it is **ubuntu**)

   e.g., `ssh -i Tina_intogen_2023.pem ubuntu@ec2-54-183-11-225.us-west-1.compute.amazonaws.com`

6. Now you will be in the instance!!

>   *See https://www.youtube.com/watch?v=30JmjvJ-DtI if more explanation is needed*

## Downloading files from AWS instance to local
`scp -i Tina_intogen_2023.pem ubuntu@ec2-54-183-11-225.us-west-1.compute.amazonaws.com:/home/ubuntu/intogen-plus/INPUTS/DCIS_new/data_mutations_extended.txt /Users/tingyang/Desktop/`

