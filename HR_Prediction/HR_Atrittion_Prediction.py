import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
model = pickle.load(open('HR_Atrittion.pkl','rb'))
app = FastAPI()

class DataIn(BaseModel):
    Age : int
    DistanceFromHome : int
    EnvironmentSatisfaction :  int
    JobInvolvement : int
    JobLevel : int
    MonthlyIncome : int
    NumCompaniesWorked : int
    PercentSalaryHike : int
    PerformanceRating : int
    RelationshipSatisfaction : int
    StandardHours : int
    StockOptionLevel : int
    TotalWorkingYears : int
    TrainingTimesLastYear : int
    WorkLifeBalance : int
    YearsAtCompany : int
    YearsInCurrentRole : int
    YearsSinceLastPromotion : int
    YearsWithCurrManager : int
    JobSatisfaction : int
    BusinessTravel_Travel_Frequently : int
    BusinessTravel_Travel_Rarely : int
    Department_Research_Development : int
    Department_Sales : int
    Gender_Male : int
    JobRole_Human_Resources : int 
    JobRole_Laboratory_Technician : int
    JobRole_Manager :  int
    JobRole_Manufacturing_Director : int
    JobRole_Research_Director : int
    JobRole_Research_Scientist : int
    JobRole_Sales_Executive : int
    JobRole_Sales_Representative : int
    MaritalStatus_Married : int
    MaritalStatus_Single : int
    OverTime_Yes : int
    
@app.get('/')
def greetings():
    return {"greeting":"Hello User"}

@app.post('/predict/')
async def create_user(dataIn : DataIn):
    data = dict(dataIn).values()
    data = np.array(list(data))
    prediction = model.predict(data.reshape(-1,36))
    return 'The predicted value is '+ str(prediction[0])

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)