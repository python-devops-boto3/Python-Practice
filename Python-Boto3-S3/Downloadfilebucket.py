import boto3

s3 = boto3.client('s3')

# Specify the filename to download from s3 bucket
filename = 'Boto3filesample.txt'
bucket_name = 'python-devops-bucket'
destname = "boto3newfile"

s3.download_file(bucket_name, filename, destname)
print("file has been download from s3")