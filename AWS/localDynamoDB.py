import boto3

client = boto3.client('dynamodb',
                      aws_access_key_id="secret",
                      aws_secret_access_key="secret".strip(),
                      region_name="us-east-1")


#s3 Stuff
# try:
#     response=client.upload_file('x.jpg','thumbnailimageusingawspython','z.jpg')
#     print(response)
# except Exception as e:
#     print(e)
# client.download_file('thumbnailimageusingawspython', 'z.jpg', 'd.jpg')
#Docs
#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
def createTable():
    response = client.create_table(TableName="Music",
                                   AttributeDefinitions=[{
                                       "AttributeName": "artist",
                                       "AttributeType": "S"
                                   }, {
                                       "AttributeName": "Song",
                                       "AttributeType": "S"
                                   }],
                                   KeySchema=[{
                                       "AttributeName": "artist",
                                       "KeyType": "HASH"
                                   }, {
                                       "AttributeName": "Song",
                                       "KeyType": "RANGE"
                                   }],
                                   ProvisionedThroughput={
                                       "ReadCapacityUnits": 10,
                                       "WriteCapacityUnits": 5
                                   })
    return response


# myTable=createTable()
# print(myTable)
fakedata = {
    'artist': {
        'S': 'Taylor'
    },
    'Song': {
        'S': 'Deleicate'
    },
    'info': {
        'M': {
            'plot': {
                'S': 'test'
            },
            'rating': {
                'N': '8'
            },
        }
    }
}


def insertItem():
    table = client.put_item(TableName="Music", Item=fakedata)


# insertItem()


def getItem():
    response = client.get_item(TableName="Music",
                               Key={
                                   'artist': {
                                       'S': 'Avril'
                                   },
                                   'Song': {
                                       'S': 'HAW'
                                   }
                               })
    print(response['Item'])


# getItem()


def updateItem():
    response = client.update_item(
        TableName="Music",
        Key={
            'artist': {
                'S': 'Taylor'
            },
            'Song': {
                'S': 'Deleicate'
            }
        },
        UpdateExpression="set info.plot=:p,info.rating=:r",
        ExpressionAttributeValues={
            ':r': {
                'N': '10'
            },
            ':p': {
                'S': 'updateTes'
            },
        })


#updateItem()


def increaseItem():
    response = client.update_item(
        TableName="Music",
        Key={
            'artist': {
                'S': 'Taylor'
            },
            'Song': {
                'S': 'Deleicate'
            }
        },
        UpdateExpression="set info.rating =  info.rating + :val",
        ExpressionAttributeValues={
            ':val': {
                'N': '10'
            },
        })


# increaseItem()


def delteItem():
    response = client.delete_item(
        TableName="Music",
        Key={
            'artist': {
                'S': 'Taylor'
            },
            'Song': {
                'S': 'Deleicate'
            }
        },
    )


# delteItem()
