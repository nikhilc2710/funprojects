import boto3
import secret
import pprint
client = boto3.resource(
    's3',
    aws_access_key_id=secret.a,
    aws_secret_access_key=secret.b,
    region_name="ap-southeast-1")
bucket=client.Bucket('thumbnailimageusingawspython')
for obj in bucket.objects.all():
    print(obj.last_modified)

