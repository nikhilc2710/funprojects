#ssmParaemters
ssm=boto3.client('ssm', aws_access_key_id=secret.a,
    aws_secret_access_key=secret.b,
    region_name="ap-southeast-1")

ssm.put_parameter(
    Name='bucketName',
    Value='thumbnailimageusingawspython',
    Type='String'
)

ssm.delete_parameter(
    Name='bucketName'
)
#display all parmaetes
parameters = ssm.describe_parameters()['Parameters']
print(parameters)