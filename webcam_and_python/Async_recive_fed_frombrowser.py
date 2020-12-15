import asyncio
import websockets
import io
from PIL import Image, ImageMode
import os
import cv2
import numpy as np
import tensorflow as tf


async def time(websocket, path):
    while True:
        message = await websocket.recv()
        image = Image.open(io.BytesIO(message))
        img=np.array(image).astype(np.float32)/255.0
        im=cv2.resize(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),(178,218))
        im=np.expand_dims(im,axis=0)
        inx=tf.lite.Interpreter(model_path="model.tflite")
        inx.allocate_tensors()
        idx=inx.get_input_details()
        odx=inx.get_output_details()
        inx.set_tensor(idx[0]['index'],im)
        inx.invoke()
        opd=inx.get_tensor(odx[0]['index'])
        print(opd)
        
        # now do with your images whatever you want. I used image.show to check it, it was spamming my monitor

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
