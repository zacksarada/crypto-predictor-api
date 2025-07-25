
import pickle
import numpy as np

def load_model(coin):
    folder = "model/"
    with open(f"{folder}{coin}_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict_prices(model, days):
    x = np.arange(days).reshape(-1, 1)
    preds = model.predict(x)
    return preds.tolist()
