from flask import Flask,render_template,request,jsonify,json
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage ,firestore

cred = credentials.Certificate('liquid-receiver-241714-firebase-adminsdk-4gd7b-89ade3a46c.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'liquid-receiver-241714.appspot.com'
})

bucket = storage.bucket()
db=firestore.client()


app = Flask(__name__)
CORS(app)
@app.route("/",  methods = ['GET'])
def welcome():
    return render_template('Hello!.html')
@app.route("/",  methods = ['POST'])
def hello():
    data=request.get_json()
    blogid=data['Blogid']
    with open (blogid+'.html','w') as x:
        x.write(data['data'])
    blob=bucket.blob(blogid+"/"+blogid)
    blob.upload_from_filename(blogid+".html")
    blob.make_public()
    blogurl=blob.public_url
    ref=db.collection(u'BlogData').document(blogid)
    ref.set({
        'Blogurl':blogurl,
        'Title':data['title'],
        'Gist':data['gist'],
        'Thumbnailurl':data['thumbnailurl']

    })


    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
# @app.route('/check_selected/', methods=['POST'])
# def get_post_json():    
#     data = request.get_json()
#     print(data)
#     return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
    app.run(debug=True)


