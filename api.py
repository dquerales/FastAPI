import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class ScoringItem(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/")
async def scoring_endpoint(item: ScoringItem):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    yhat = model.predict(df)
    return {"prediction": str(yhat)}
