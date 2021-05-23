import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import gspread

cred = credentials.Certificate("nexstoc-8fb29-firebase-adminsdk-ci9dn-c64928c008.json")
firebase_admin.initialize_app(cred)
gc = gspread.service_account('t.json')
sh = gc.open("test").sheet1
# sh.share('testnextsoc@gmail.com', perm_type='user', role='writer')
# row=['email','name','phone','privileges','designation']
# sh.insert_row(row,1)

db = firestore.client()
users_ref = db.collection(u'Users')
docs = users_ref.stream()
users=[doc.to_dict() for doc in docs]
import time
for idx,value in enumerate(users):
    sh.insert_row([value['email'],value['name'],value['phone'],value['designation'],"\n".join(value['privileges'])],idx+2)
    time.sleep(0.5)




