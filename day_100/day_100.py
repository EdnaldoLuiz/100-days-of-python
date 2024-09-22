from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

base_path = os.path.abspath(os.path.dirname(__file__))
assets_path = os.path.join(base_path, 'assets')
model_path = os.path.join(assets_path, 'model.pkl')

modelo = joblib.load(model_path)
app = FastAPI()

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisData):
    df = pd.DataFrame([data.dict()])
    df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    pred = modelo.predict(df)
    
    classes = ['setosa', 'versicolor', 'virginica']
    result = classes[pred[0]]
    
    return {"prediction": result}