from fastapi import FastAPI, Request
import uvicorn
import os
from classifier.model import predict_model
from tensorflow.keras.models import load_model
import json
import numpy as np


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

n_class = 10  # Set Number of Classes to your target
model_name = 'model'

model = load_model(f'{ROOT_DIR}/classifier/models/{model_name}.h5')

app = FastAPI()


@app.post('/predict')
async def hello(data: Request):

    jsonData = await data.json()
    data = json.loads(jsonData['data'])

    result = predict_model(model, np.array([data]), n_class)

    return {'status': 'Success', "result": result.tolist()}


if __name__ == '__main__':
    uvicorn.run(app)
