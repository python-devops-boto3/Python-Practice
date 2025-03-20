import boto3

# Create an S3 Client
s3 = boto3.client('s3')

# List all AWS Bucket 
response = s3.list_buckets()
#print(response)
#print(response["Buckets"])

for i in response["Buckets"]:
    print(i["Name"])