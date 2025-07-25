from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_model, predict_prices

app = FastAPI()

class PredictRequest(BaseModel):
    coin: str
    days: int

@app.post("/predict")
def predict(req: PredictRequest):
    coin = req.coin.upper()
    model = load_model(coin)
    result = predict_prices(model, req.days)
    return {"predicted_price": result}
