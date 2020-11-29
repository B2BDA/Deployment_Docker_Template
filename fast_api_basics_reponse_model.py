# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:42:36 2020

@author: bishw
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

class DataIn(BaseModel):
    Name: str
    Email: EmailStr
    Age: int
    Password: str
    
class DataOut(BaseModel):
    Name: str
    Email: EmailStr
    Age: int

@app.get('/')
def greetings():
    return {"greeting":"Hello User"}

@app.post('/create/', response_model=DataOut)
async def create_user(dataIn : DataIn):
    return dataIn

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)
    