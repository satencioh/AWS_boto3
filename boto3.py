import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='your key’,
aws_secret_access_key='your secret'
)
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
srcbucket = s3.Bucket('nombre del bucket')
destbucket = s3.Bucket('mi bucket')
dest_files = [file.key for file in srcbucket.objects.all()
# Iterate All Objects in Your S3 Bucket Over the for Loop
for file in srcbucket.objects.all():
print(file)