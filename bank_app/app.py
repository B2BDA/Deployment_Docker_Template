from flask import Flask, request
import pandas as pd
import pickle
# from tensorflow import keras
import numpy as np
# model = keras.models.load_model('bank_note_auth.h5')
model = pickle.load(open('bank_auth.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome All"
@app.route('/predict', methods = ['GET'])
def prediction():
    var = request.args.get('var')
    skw = request.args.get('skw')
    kur = request.args.get('kur')
    etp = request.args.get('etp')
    pred = model.predict(np.array([[var, skw, kur, etp]],dtype = np.float32 ))
    return 'The predicted value is '+ str(pred[0])
@app.route('/predict_from_file', methods = ['POST'])
def prediction_from_file():
    df = pd.read_csv(request.files.get('file'))
    pred = model.predict(df)
    return 'The predicted values are '+ str(pred)
if __name__ == '__main__':
    app.run()
