import sys
from io import StringIO
import contextlib
import traceback
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# cred = credentials.Certificate('votingapp-54505-firebase-adminsdk-t4orc-a9445ccbfa.json')
# firebase_admin.initialize_app(cred)
# db=firestore.client()
# ref=db.collection(u'Compiler').document(u'testing')
@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

code = """
from collections import Counter
def squ(x):
    return x*x
y=list(map(squ,[1,2,3,4,5,6]))
print(y)
"""
with stdoutIO() as s:
    try:
        exec(code)
    except:
        print(sys.exc_info())
print(s.getvalue())
# ref.set({'output':s.getvalue()})