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
    #uncomment in lambda else comment
    # if 'queryStringParameters' in event and event['queryStringParameters'] is not None:
    #     if 'dragonName' (paramneter name passed in url parameter) in event['queryStringParameters']:
    #         expression = "select * from S3Object[*][*] s where s.dragon_name_str =  '" + event["queryStringParameters"]['dragonName'] + "'"
    #     if 'family' in event['queryStringParameters']:
    #         expression = "select * from S3Object[*][*] s where s.family_str =  '" + event["queryStringParameters"]['family'] + "'"
    #     if "locationcountry" in event['queryStringParameters']:
    #         expression="select * from S3Object[*][*] s where s.location_country_str =  '" + event["queryStringParameters"]['locationcountry'] + "'"

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

