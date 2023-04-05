import uvicorn
from fastapi import FastAPI
from model import CreditModel, CustomerData

# Create app and model objets
app = FastAPI()
model = CreditModel()

# Expose the prediction functionality, make a prediction from the passed
# JSON data and return the probability of defaulting with the confidence
@app.post("/predict")
def predict_proba(customer_data: CustomerData):
    probability = model.predict_score(customer_data)
    return {"score": probability}

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

