from fastapi import FastAPI,Request
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    name:str
    price:float
    is_offfer:Optional[bool]=False
from random import randint
abc=0
@app.get("/")
def read_root():
    global abc
    abc+=1
    return {'key': f'{abc}'}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None,test: Optional[str]=None):
#     return {"item_id": item_id, "q": q,'My_string':test}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

@app.post("/")
async def post_method (request: Request):
    x=await request.json()
    print(x['url'])

    return {"response": "OK"}
