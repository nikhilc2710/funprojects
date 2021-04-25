import subprocess
import os
import time
from io import StringIO
from fastapi import FastAPI
import uvicorn
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

commands={'python':['python','test.py'],'cpp':['g++','hello.cpp','-o','a']}
def execProgram(ip):
    child = subprocess.Popen(['./a'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=False)
    try:
        out,err=child.communicate(ip.encode(),timeout=2)
        os.remove('a')
        os.remove('hello.cpp')

    except subprocess.TimeoutExpired:
        return {'Error':'TLE'}
    finally:
        child.kill()
        outs, errs = child.communicate()
    return {'output':{'stdout':out,'stderr':err}}

def main(lang,ip,code):
    if lang=='python' or lang=='Python':
        with StringIO(code) as f:
            child=subprocess.Popen(['python','-c',f.read()], stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=False)
            try:
                out,err=child.communicate(ip.encode(),timeout=2)
                return {'output':{'stdout':out,'stderr':err}}
            except Exception as e:
                print(e)
                return {'Error':'TLE'}
            finally:
                child.kill()
                outs, errs = child.communicate()
    if lang=='cpp' or lang=='c++':
        child = subprocess.Popen(commands[lang], stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        child.wait()
        out,err=child.communicate()
        if err:
            return {'Error':err}
        else:
            return execProgram(ip)
def bridge(ext: str,code: str,stdip: str = ""):
    if ext=='python':
        op=main('python',stdip,code)
        return op
        
        
    if ext=='cpp':
        with open('hello.cpp','w+') as f:
            f.write(code)
        op=main(ext,stdip,"")
        return op

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
async def home(request:Request):
    x=await request.json()
    print(x)
    res=bridge(x['lng'],x['code'],x['stdip'])
    return res