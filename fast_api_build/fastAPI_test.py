from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn
import numpy as np
model = pickle.load(open('bank_auth.pkl','rb'))
class Input(BaseModel):
    var: float
    skw: float
    kur: float
    etp: float

app = FastAPI()

@app.get('/')
async def welcome():
    return "Welcome All"

@app.post("/predict/")
async def prediction(input_val: Input):
    a = type(input_val)
    pred = model.predict(np.array([[input_val.var, input_val.skw, input_val.kur, input_val.etp]],dtype = np.float32 ))
    return 'The predicted value is '+ str(pred[0])
