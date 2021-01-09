import boto3
import secret
import pprint
client = boto3.resource(
    's3',
    aws_access_key_id=secret.a,
    aws_secret_access_key=secret.b,
    region_name="ap-southeast-1").meta.client
ssm=boto3.client('ssm', aws_access_key_id=secret.a,
    aws_secret_access_key=secret.b,
    region_name="ap-southeast-1")
bucket='thumbnailimageusingawspython'
bucketname=ssm.get_parameter(Name="bucketName")['Parameter']['Value']
filename=ssm.get_parameter(Name="fileName")['Parameter']['Value']


def jsonContent():
    expression="select * from s3object s"

    result=client.select_object_content(
        Bucket=bucketname,
        Key=filename,
        ExpressionType='SQL',
        Expression=expression,
        InputSerialization={'JSON':{'Type':'Document'}},
        OutputSerialization={'JSON':{}}
    )
    for event in result['Payload']:
        if 'Records' in event:
            print(event['Records']['Payload'].decode('utf-8'))
jsonContent()

#get all objects
# for obj in bucket.objects.all():
#     print(obj.last_modified)

