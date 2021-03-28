
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("x.json")
firebase_admin.initialize_app(cred)

d=firestore.client()
city_ref = d.collection(u'testing').document(u'tandori zinger')
batch = d.batch()
# x=city_ref.get()
# if x.exists:
#     city_ref.update({'quantity':firestore.Increment(50)})
# else:
#     city_ref.set({'price':600,'quantity':10},merge=True)
#get all docs
# docs = d.collection(u'testing').stream()
# for i in docs:
#     print(i.id,i.to_dict())

# city_ref.update({u'Orders': firestore.ArrayUnion([u'ffd'])})

# city_ref.set(
#     {'bucket8':{'quantity':firestore.Increment(1)}},merge=True
# )

# x=city_ref.get()
# if x.exists:
#     print(x.to_dict())
#batch operations firesotre
# for i in ['big8','chichkenpizza','tandori zinger']:
#     sf_ref = d.collection(u'testing').document(i)
#     batch.update(sf_ref, {u'quantity': firestore.Increment(69696996)})
# batch.commit()
transaction = d.transaction()
# city_ref = db.collection(u'cities').document(u'SF')

@firestore.transactional
def update_in_transaction(transaction,document):
    # for i in docs:
    ref=d.collection(u'testing').document(document)
    if ref.get().exists:
        snapshot = ref.get(transaction=transaction)
        transaction.update(ref,{u'quantity':snapshot.get(u'quantity')+10})
        return
    else:
        d.collection(u'testing').document(i).set({'quantity':1,'cost':50},merge=True)
        return
# update_in_transaction(transaction,['big8','chichkenpizza','Chichen Tripple Rice'])
for i in ['big8','chichkenpizza','Chichen Tripple Rice','big8','chicken chilli']:
    update_in_transaction(transaction,i)

# result = update_in_transaction(transaction, city_ref)
# if result:
#     print(u'Population updated')
# else:
#     print(u'Sorry! Population is too big.')