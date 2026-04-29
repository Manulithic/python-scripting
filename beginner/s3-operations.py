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
