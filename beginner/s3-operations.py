######SCRIPT-1########
######LIST ALL BUCKETS WITH ARN#######

#!/usr/bin/python3

import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:
  bucket_name = bucket['Name']
  bucket_arn = bucket['BucketArn']
  print(bucket_name, bucket_arn)

----------------------------------------------------------------------------------
######SCRIPT-2########
######LIST BUCKET ARN & CREATION DATE WITH BUCKET NAME AS INPUT#######

#!/usr/bin/python3

import boto3
import sys

names = sys.argv[1:]
s3 = boto3.client('s3')
response = s3.list_buckets()

if len(names) < 1:
  print("ERROR: Please Enter Bucket Name to fetch Details.")
  print("USAGE: python3 fetch-bucket-details.py <BUCKET-NAME>")
  
for name in names:
  for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    bucket_arn = bucket['BucketArn']
    bucket_creation_date = bucket['CreationDate']
    if bucket_name == name:
      print(bucket_name, bucket_arn, bucket_creation_date)

----------------------------------------------------------------------------------
######SCRIPT-3########
######CREATE S3 BUCKET#######
#!/usr/bin/python3

import boto3
import hashlib
import random
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

s3 = boto3.client('s3', region_name='ap-south-1')
customer_name = sys.argv[1].lower()

if len(sys.argv) != 2:
    logger.info("Error:Bucket Name not passed")
    print("Usage: python3 create_s3.py <customer-name>")

random_number = random.randint(1000, 999999)

hash_object = hashlib.md5(str(random_number).encode())

random_id = hash_object.hexdigest()[:6]

bucket_name = f"cust-{customer_name}-{random_id}"

logger.info(f"creating bucket {bucket_name}")

try:
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
    logger.info(f"created bucket {bucket_name} successfully")
except Exception as e:
    logger.info(f"ERROR: CREATING BUCKET: {str(e)}")


----------------------------------------------------------------------------------
######SCRIPT-4########
######CHECK IF OBJECT EXISTS IN S3 BUCKET#######
----------------------------------------------------------------------------------

#!/usr/bin/python3


import boto3
import logging
import sys
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_object(bucket_name, file_name):
    try:
        s3.head_object(Bucket=bucket_name, Key=file_name)
        logger.info(f"found object {file_name} in bucket {bucket_name}")
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            logger.info(f"object {file_name} not found")
            return False
        raise

def main():
    bucket_name = sys.argv[1]
    file_name = sys.argv[2]
    check_object(bucket_name, file_name)

if __name__ == "__main__":
    main()
