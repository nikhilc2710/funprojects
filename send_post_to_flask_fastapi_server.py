# import requests
# import json
#FCM Token
# payload = {
#  "notification": {
#  "title": "Hey there", 
#  "body": "Mobile check"
#  },
#  "to" :"el-8P3oPU_ahSp6c0kpfou:APA912HvqW8gVHoBiHaeK3er4c9s"
# }
# head={ 'content-type': "application/json",
#     'authorization': "key=AAA-jnE:APA91bFHken2X1z_kHAwXjeMRvPftRRAXFT9nBWS4wzSHlOkq3h7ayaldecX6SWl4GD7Y3qZ837zhwn9AiQF",
#     'cache-control': "no-cache",
#     'postman-token': "1e7e57b164"
# }
# res=requests.post('https://fcm.googleapis.com/fcm/send',data=json.dumps(payload),headers=head)
# print(res.text)
#Flask Server
# import requests
import json
# payload = {
# "list":['url1','url2']}
# print('hello')
# res=requests.post('hosted or local host',data=json.dumps(payload))
# print(res.text)

#FAST API SERVER

import requests
import json
payload = {
"url":'url'}
res=requests.post('https://7s4rj3apid.execute-api.ap-southeast-1.amazonaws.com/test/resttest',data=json.dumps(payload))
x=res.json()
print(x)
