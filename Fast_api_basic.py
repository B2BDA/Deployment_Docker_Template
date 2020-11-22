from fastapi import FastAPI
import uvicorn
from post_data import Sample
app = FastAPI()

@app.get("/")
async def welcome():
    return {'message':'Hello World!'}
    
@app.get("/Welcome")
async def greeting(name:str):
    return {"Welcome": name}

@app.post("/Data")
async def details(data:Sample):
    data = data.dict()
    return {'DATA':f'{data}'}
  
if __name__ == '__main__':
    uvicorn.run(app, port = 8000, host = '127.0.0.1')
    
# in console type uvicorn name_of_api:app --reload
# use /docs or /redoc to try passing to a ppost req