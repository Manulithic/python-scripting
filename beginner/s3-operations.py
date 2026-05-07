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
