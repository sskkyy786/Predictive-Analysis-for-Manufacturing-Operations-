import numpy as np
import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from io import StringIO
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = FastAPI()

model = None
X_train, X_test, y_train, y_test = None, None, None, None

# upload endpoint
@app.post("/upload")
async def uploadfile(file: UploadFile):
    
    data1 = await file.read()
    global df
    df = pd.read_csv(StringIO(data1.decode("utf-8")))

    if df.empty:
        raise HTTPException(status_code=400, detail="Invalid/empty file...")

    return {"message": "Uploaded"}

# training endpoint
@app.post("/train")
async def trainerr():
    global model, X_train, X_test, y_train, y_test
    
    X = df[  # segregating dataset into training inputs and labels 
        [
            "ProductionVolume",
            "ProductionCost",
            "SupplierQuality",
            "DeliveryDelay",
            "DefectRate",
            "QualityScore",
            "MaintenanceHours",
            "DowntimePercentage",
            "InventoryTurnover",
            "StockoutRate",
            "WorkerProductivity",
            "SafetyIncidents",
            "EnergyConsumption",
            "EnergyEfficiency",
            "AdditiveProcessTime",
            "AdditiveMaterialCost",
        ]
    ]
    y = df["DefectStatus"]

    X = np.array(X.values)
    y = np.array(y.values)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12314)

    # decision tree was my final model of choice as it gave the highest accuracy compared to the other models I experimented with
    # which included MLP and a logistic regression model
    model = DecisionTreeClassifier(max_depth=5, random_state=12314) 
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    return {"message": "Training complete.", "accuracy": acc}

class PredRequest(BaseModel):
    ProductionVolume: float
    ProductionCost: float
    SupplierQuality: float
    DeliveryDelay: float
    DefectRate: float
    QualityScore: float
    MaintenanceHours: float
    DowntimePercentage: float
    InventoryTurnover: float
    StockoutRate: float
    WorkerProductivity: float
    SafetyIncidents: float
    EnergyConsumption: float
    EnergyEfficiency: float
    AdditiveProcessTime: float
    AdditiveMaterialCost: float

# final prediction endpoint post training
@app.post("/predict")
async def predict(data: PredRequest):
    global model

    dat = np.array([[getattr(data, field) for field in data.__fields__.keys()]])
    pred = model.predict(dat)
    confidence = model.predict_proba(dat).max()

    result = {"DefectStatus": int(pred[0]), "Confidence": confidence}
    return JSONResponse(content=result)