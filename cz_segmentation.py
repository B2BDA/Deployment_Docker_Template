# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:56:51 2020

@author: bishw
"""
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn
# import numpy as np
from fastapi.encoders import jsonable_encoder
fake_db = {}
model = pickle.load(open(r"C:\Users\bishw\Downloads\Compressed\MODEL\cluster.pkl","rb")) 
app = FastAPI(title='Customer Segmentation APP')

class DataIn(BaseModel):
    recency: float = 0
    frequency: float = 0
    revenue: float = 0

@app.get('/')
async def greeting():
    return {"message":"Hello User."}

# @app.get('/Segment1/{recency}/{frequency}/{revenue}')
# async def cluster(recency:int, frequency:int, revenue:int):
#     cluster_class = model.predict(np.array([[recency, frequency, revenue]], dtype=np.float64))
#     return cluster_class

@app.post('/Segment/')
async def cluster(dataIn:DataIn):
    json_compatible_item_data = jsonable_encoder(dataIn)
    cluster_class = model.predict([[json_compatible_item_data.get('recency'), json_compatible_item_data.get('frequency'), json_compatible_item_data.get('revenue')]])
    cluster_details = {3:'High Revenue/Frequency, Less Recency', 0:'High Revenue/Frequency, Less Recency',2:'Low Revenue/Frequency, High Recency', 1:'Medium Revenue/Frequency, Medium Recency'}
    return 'The cx is likely to be  '+ str(cluster_details.get(cluster_class[0]))
    
if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)