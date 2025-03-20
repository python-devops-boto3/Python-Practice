import boto3

s3 = boto3.client("s3")

# bucket name 
bucket_name = "python-practice-boto3"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    },
)
print(f"This {bucket_name} created successfully")
