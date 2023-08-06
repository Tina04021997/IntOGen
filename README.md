# IntOGen under AWS
## Creating IntOGen inputs
The input files are **metadata.bginfo** and **data_mutations_extended.txt**
1. metadata.bginfo:
   Change every time for "PLATFORM", "CANCER", and "GENOMERF"
2. data_mutations_extended.txt:
   

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
1. Create the intogen bash script `sample.sh` under intogen-plus folder
2. Run the script:
   - Create a new screen
   - do `conda activate intogenbuild`
   - do `sort -V data_mutations_extended.txt` before running IntOGen
   - go to intogen-plus folder and change your bash file's permission by `chmod +x sample.sh`
   - do `./sample.sh > ~/intogen-plus/ERRORandOUTPUTs/output.txt 2>~/intogen-plus/ERRORandOUTPUTs/error.txt`

   > *Note: The fisrt arrow will store the standard output and the second arrow will store the standard error*

## Creating key pairs
1. Create an instance and at the Key pair section, create a new key
2. You will get a pem file, place it on your local desktop
3. On the terminal, do `chmod 400 Tina_intogen_2023.pem` to change the permission
4. Go back to your AWS instance and copy the *Public IPv4 DNS* Address
5. In your terminal, go to where you put your key and than do `ssh -i Tina_intogen_2023.pem ubuntu@{IPv4 address}` (make sure it is **ubuntu**)

   e.g., `ssh -i Tina_intogen_2023.pem ubuntu@ec2-54-183-11-225.us-west-1.compute.amazonaws.com`

6. Now you will be in the instance!!

>   *See https://www.youtube.com/watch?v=30JmjvJ-DtI if more explanation is needed*

## Output file interpretation
1. Go to `./run_files/output/sample/` and get `drivers.tsv`
2. Remove genes that are:
   - “combination” (too weak to be called as driver genes, not enough evidence called by the 7 callers)
	- q-value combination score > 0.05

## Downloading files from AWS instance to local
`scp -i Tina_intogen_2023.pem ubuntu@ec2-54-183-11-225.us-west-1.compute.amazonaws.com:/home/ubuntu/intogen-plus/INPUTS/DCIS_new/data_mutations_extended.txt /Users/tingyang/Desktop/`

## Uploading files from local to AWS instance
`scp -i Tina_intogen_2023.pem /Users/tingyang/Desktop/IntOGen_OL/input_LK/data_mutations_extended.txt ubuntu@ec2-52-53-197-38.us-west-1.compute.amazonaws.com:/home/ubuntu/intogen-plus/INPUTS/LK`

## Extra notes
1. Before terminate any instance, all the files in the hardware will disappear so download everything you need before terminate any instances
2. Go to AWS volumn and put your name in the tag and remember to shut down the instance attached volumn after terminating the insaance if needed

