import boto3

client = boto3.client(
    's3',
    'dynmodb'
    aws_access_key_id="Some thing i Know",
    aws_secret_access_key="Lol u messed up XD :)",
    region_name="us-east-1"
)
# try:
#     response=client.upload_file('x.jpg','thumbnailimageusingawspython','z.jpg')
#     print(response)
# except Exception as e:
#     print(e)
client.download_file('thumbnailimageusingawspython', 'z.jpg', 'd.jpg')