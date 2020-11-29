# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:22:16 2020

@author: bishw
"""

# creating a fun api which will help me to remember the various optimizers in ANN
import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(description='Optimizers')

@app.get('/Welcome')
async def greeting():
    return {'greeting_message':'Welcome to Optimizer App'}

@app.get('/SGDM')
def sgdm():
    return {'method':'instead of calc the derivative of loss wrt weight, we take the EWMA Vdwt = b x Vdwt-1 + (1-b) x dl/dw t-1'}
@app.get('/ADAGRAD')
def adagard():
    return {'method':'instead of keeping the lr fixed, we can calc the lr using lr/srqt(at+e) where e is a small +ve number in order to prevent zero div error and at = sq. summation of all the loss term'}
@app.get('/ADADELTA')
def adadelta():
    return {'method':'instead of calc the at like in AGADRAG, we can calc the EWMA of the sq.loss term Sdt = b x sdt-1 + (1-b) x sq(dl/dw)'}
@app.get('/ADAM's)
def adam():
    return {'method':'here we mix the adadelta and the sdgm'}

# def sgdm():
#     return {'method':'instead of calc the derivative of loss wrt weight, we take the EWMA Vdwt = b x Vdwt-1 + (1-b) x dl/dw t-1'}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000)