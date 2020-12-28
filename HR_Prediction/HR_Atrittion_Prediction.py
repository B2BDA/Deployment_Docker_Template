import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
model = pickle.load(open('HR_Atrittion1.pkl','rb'))
encoder = pickle.load(open('encoder.pkl','rb'))

app = FastAPI()

class DataIn(BaseModel):
    
    Age: int
    DistanceFromHome: int
    EnvironmentSatisfaction: int
    JobInvolvement: int
    JobLevel: int
    JobSatisfaction: int
    MonthlyIncome: int
    NumCompaniesWorked: int
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StandardHours: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int
    BusinessTravel: str
    Department: str
    Gender: str
    JobRole: str
    MaritalStatus: str
    OverTime: str
    
@app.get('/')
async def greetings():
    return {"greeting":"Hello User"}

@app.post('/predict/')
async def create_user(dataIn : DataIn):
    data = dict(dataIn).values()
    data1 = np.array(list(data)[0:20]).reshape(1,-1)
    data2 = encoder.transform(np.array(list(data)[20:]).reshape(1,-1))
    data =  np.hstack((data1, data2))
    prediction = model.predict_proba(data)
    return 'There is a probability of '+ str(prediction[0][1]) + '  the employee leaving the org'

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)