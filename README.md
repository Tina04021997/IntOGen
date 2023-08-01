# AWS
## Using AWS

## Creating key pairs
1. Create an instance and at the Key pair section, create a new key
2. You will get a pem file, place it on your local desktop
3. On the terminal, do `chmod 400 Tina_intogen_2023.pem` to change the permission
4. Go back to your AWS instance and copy the *Public IPv4 DNS* address
5. In your terminal, do `ssh -i Tina_intogen_2023.pem ubuntu@{IPv4 address}` (make sure it is **ubuntu**)

   e.g., `ssh -i Tina_intogen_2023.pem ubuntu@ec2-54-183-11-225.us-west-1.compute.amazonaws.com`

6. Now you will be in the instance!!

>   *See https://www.youtube.com/watch?v=30JmjvJ-DtI if more explanation is needed*

