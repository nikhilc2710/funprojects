import subprocess
import os
import time
from fastapi import FastAPI
import uvicorn
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

commands={'python':['python','test.py'],'cpp':['g++','hello.cpp','-o','a']}
def  execProgram(ip):
    child = subprocess.Popen(['./a'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=False)
    try:
        out,err=child.communicate(ip.encode(),timeout=2)
        os.remove('a')
        os.remove('hello.cpp')

    except subprocess.TimeoutExpired:
        return "TimeOut"
    return out.decode('utf-8'),err.decode('utf-8')

def  main(lang,ip):
    if lang=='python' or lang=='Python':
        child = subprocess.Popen(commands[lang], stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        try:
            out,err=child.communicate(ip.encode(),timeout=2)
            os.remove('test.py')
            return out.decode('utf-8'),err.decode('utf-8')
        except subprocess.TimeoutExpired:
            return 'TimeOut'
    if lang=='cpp' or lang=='c++':
        child = subprocess.Popen(commands[lang], stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False)
        child.wait()
        out,err=child.communicate()
        if err:
            return {'error':err.decode('utf-8')}
        else:
            return   execProgram(ip)

def  bridge(ext: str,code: str,stdip: str = ""):
    if ext=='python':
        with open('test.py','w+') as f:
            f.write(code)
        op=  main(ext,stdip)
        return {'output':op}
        
        
    if ext=='cpp':
        with open('hello.cpp','w+') as f:
            f.write(code)
        op=  main(ext,stdip)
        return {'output':op}


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
    res=  bridge(x['lng'],x['code'],x['stdip'])
    return res

@app.get('/')
async def home():
    return "OK"
if __name__ == "__main__":
    uvicorn.run(app, port=8000)