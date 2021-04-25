from flask import Flask
from flask import request
import json
from flask import Response
from flask_cors import CORS
import io
from PIL import Image, ImageMode
import base64
from collections import defaultdict
from itertools import chain
from random import choice
import firebase_admin
from firebase_admin import credentials,firestore
from pyzbar import pyzbar
import os

app = Flask(__name__)
CORS(app)



cred = credentials.Certificate("x.json")
firebase_admin.initialize_app(cred)

d=firestore.client()
transaction = d.transaction()


@firestore.transactional
def update_in_transaction(transaction,name,price,quantity,dd):

	# for i in docs:
	ref=d.collection('testing').document(name)
	if ref.get().exists:
		snapshot = ref.get(transaction=transaction)
		currval=snapshot.get(u'quantity')
		transaction.update(ref,{u'quantity':currval+quantity,u'cost':price})
		dd[name]=(currval+quantity)
		return
	else:
		dd[name]=quantity
		d.collection(u'testing').document(name).set({'quantity':quantity,'cost':price},merge=True)
		return

@app.route('/', methods=['GET', 'POST'])
def login():
	dd=defaultdict(int)
	if request.method == 'POST':
		x=json.loads(request.data)
		img=base64.b64decode(x['data'][23:])
		imgx=Image.open(io.BytesIO(img))
		barcodes = pyzbar.decode(imgx)
		arr=[[x for x  in i.data.decode('ascii').strip().split('\n')] for i in barcodes]
		arr=[i for i in chain(*arr)]
		for prods in arr:
			x=prods.split(':')
			update_in_transaction(transaction,x[0],int(x[1]),int(x[2]),dd)
		return json.dumps(dd)
	else:
		print(request.method)
		return Response(status=401)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host="0.0.0.0",port=port)