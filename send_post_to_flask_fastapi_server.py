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

token="eyJraWQiOiJ3aEo1aERVQUdDeFwvR1B3dEJhREZGRytaYkhwcktBNkpKZXF4aXZEUFdoMD0iLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiZVFEMV82aW5JeGdtcXlEQS1aVDN5USIsInN1YiI6ImI3NmEzNWYwLTdiMDEtNDU5NS04NTE0LTgzZWNkYzcwZThmYyIsImF1ZCI6Ijc0cTc0MnMxMHYwcGRqb2o0cGxrZms0YmhzIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjEwMjU2NjI0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfMHpFazJub2ZWIiwiY29nbml0bzp1c2VybmFtZSI6InRlc3RVU0VSIiwiZXhwIjoxNjEwMjYwMjI0LCJpYXQiOjE2MTAyNTY2MjQsImVtYWlsIjoid29vZHJhbmdlMkBnbWFpbC5jb20ifQ.knXM_A7OLN6S4IpK8vBclvCnVTn3JADzll7Gko96MU18RM5pYi01ljcGDQMqRu9Wqus1rWUZDSFq8tyB8LMT77RbSBi7rvTaGzJ-2iW9sFLKO3k_Dt2juCfO27hEA95Ixwa2V2gErTQ1esWvDC0H6PdsOotLdOoJb3oYDDFi_29dbxmxSpxVEZzi8Ii6i79WYeMU5rOLPaIUSgrY-Ms43bvT9jLl6U6NOHR3UYOxLCxCFq5eIgqbu1VSz3xwVweADD2Ekt7OPjhihSzXqVWJRo9qNCdibxv_ef-ECw3BYFG_G0LUAFtVXOJLdDD0gd_v7aCTDdaRvFudlSjSiRU5JA&access_token=eyJraWQiOiJDWjNMY2dORzAxQ081NE1zcG9lOFNqS0lLNHUyVHBRY0p1SHE0NXUwSm5vPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiNzZhMzVmMC03YjAxLTQ1OTUtODUxNC04M2VjZGM3MGU4ZmMiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNjEwMjU2NjI0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfMHpFazJub2ZWIiwiZXhwIjoxNjEwMjYwMjI0LCJpYXQiOjE2MTAyNTY2MjQsInZlcnNpb24iOjIsImp0aSI6Ijk1NjA0YTQ5LWRhMDgtNDM4NC04ODJhLWMwNDAxMzRkNzAyZSIsImNsaWVudF9pZCI6Ijc0cTc0MnMxMHYwcGRqb2o0cGxrZms0YmhzIiwidXNlcm5hbWUiOiJ0ZXN0VVNFUiJ9.fZIETrrvG9_Cho4Cmztoz4u1rMp-K9juLOCFh9lHedOiPFNPf2UVHxgxhZEMyBI3N_k5kbr4iuhaXb8Rmvf2x3gDbTjj11OGiy2JPHW7_32eOs-3U9BwH63eU17LgU1ZRZjJKeCuY2zOD6RJmlgjoRTmEBHPU7RVJY2SLsB7eSXZrE8Rub3aZL38sBTdBVtMEtQYaDs4_fPHcOgoYW1goyKlT-MN5XAxB7tdij2eK5UIMg6FSjhA0-1QlFd5_QHvksJYTKRtIs2NxfcUlzPN8jOj8e0SeYIsWkdCKamzmrUpiIX0oJhXe1u8SzFAnndA7GUfxe1o_7UNpetH-5jcAQ"
head={
    'Authorization':token
}
res=requests.get(url="https://twxj3alru3.execute-api.ap-southeast-1.amazonaws.com/getpostTest/dragons",headers=head)
x=res.json()
print(x)
