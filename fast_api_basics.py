# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

class GetDataIn(BaseModel):
    Emp_Pass: int
    Name: str
    Age: float
    Designation: Optional[str] = None
    
class GetData(BaseModel):
    Name: str
    Age: float
    Designation: Optional[str] = None
    
app = FastAPI()
# get request to fetch data from server
@app.get('/')
async def welcome_page():
    return {"message":"hello"}

# passing a param in the url
@app.get('/details/{Name}/{age}')
async def details(Name:str, age:int):
    return {"message":f"Welcome {Name} of {age} "}
    
# query params where the URL will look like a question
@app.get('/details2')
async def details2(Name: str, age: Optional[int]): # optional means it is not requried to fill. It only works with str dtype
    return {"message": f"Welcome {Name} and you are {age} years old mate"}

# the trigger url will look something like this http://127.0.0.1:8000/details2?Name=asdGV&age=12

# user /docs for better understanding which is SwaggerUI / OpenAPI and more like a postman

# post request - to make new data inside the server
@app.post('/details3')
async def details3(getData: GetData):
    getData = getData.dict()
    return {'Details':f'{getData}'}

# mixing post with url params
@app.post('/details4/{emp_id}')
async def details4(getData:GetData, emp_id:int, active:bool):
    return {'Employee Code':emp_id, 'Details':f'{getData}', 'Status':active}

# reponse model is when we want to limit what the user can see for example like password 
@app.post('/details5/', response_model = GetData, response_model_exclude = {'Designation'}) # we can also use include which will include that field only
# response_model is what the user will be able to see but we are taking in data from GetDataIn
async def details5(getData: GetDataIn):
    return getData

if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='localhost')

