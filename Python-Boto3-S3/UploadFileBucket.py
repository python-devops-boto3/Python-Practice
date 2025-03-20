import boto3

s3 = boto3.client('s3')

#specify the file to upload in bucket
filename = 'Boto3file.txt'
bucket_name = 'python-devops-bucket'
destfile = 'botonewfile'

s3.upload_file(filename, bucket_name, destfile)
print("file has been uploaded successfully")
