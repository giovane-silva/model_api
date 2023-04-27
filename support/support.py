import joblib
import pandas as pd

def load_model():
    return joblib.load("./artifacts/model.joblib")

def predict(model, data):
    prediction = model.predict_proba(pd.DataFrame(data, index = [0]))[:, 1]
    return 'died' if int(round(prediction.tolist()[0])) <= 0.5 else 'lived', round(prediction.tolist()[0], 2)