# Manufacturing Defects Prediction API

**Model**: Decision Tree, I had experimented with various types of models and hyperparameter values and had finally chosen this model as it gave the highest accuracy. 

This API uses a  model to predict manufacturing defects based on input features. It includes endpoints for uploading data, training the model, and making predictions.

---

## Features

- **Upload Dataset** (POST /upload): To upload the CSV file dataset to be used for training.
- **Train Model** (POST /train): To execute model training using the uploaded dataset.
- **Make Predictions** (POST /predict): To give input values in JSON format to get predictions in JSON format.

---

## Setup Instructions

### Step 1: Clone this Repository
Download or clone the API codebase to your local machine.
```bash

git clone https://github.com/sskkyy786/Predictive-Analysis-for-Manufacturing-Operations-.git

cd https://github.com/sskkyy786/Predictive-Analysis-for-Manufacturing-Operations-.git
```

### Step 2: Install Dependencies
Install the necessary Python packages:
```bash
pip install fastapi uvicorn scikit-learn pandas numpy
```

---

## Running the API

Run the following command to start the FastAPI server:
```bash
uvicorn api:app --reload
```

## API Endpoints

### 1. **Upload Dataset (POST /upload)**

To upload a CSV file containing the dataset. You can use Postman for this.

Attach the CSV file under the 'file' key in the request body.

#### Example Response:
```json
{
    "message": "Uploaded",
}
```

### 2. **Train Model (POST /train)**
Train the Decision Tree model using the uploaded dataset. No additional input is required for this endpoint.

#### Example Response:
```json
{
    "message": "Training complete.",
    "accuracy": 0.85
}
```

### 3. **Make Predictions (POST /predict)**
Provide input values to get predictions for manufacturing defects.

#### Input Format:
Send a JSON object with the following structure:
```json
{
    "ProductionVolume": 100,
    "ProductionCost": 2000,
    "SupplierQuality": 80,
    "DeliveryDelay": 10,
    "DefectRate": 0.05,
    "QualityScore": 90,
    "MaintenanceHours": 15,
    "DowntimePercentage": 5,
    "InventoryTurnover": 30,
    "StockoutRate": 0.1,
    "WorkerProductivity": 85,
    "SafetyIncidents": 1,
    "EnergyConsumption": 500,
    "EnergyEfficiency": 0.95,
    "AdditiveProcessTime": 25,
    "AdditiveMaterialCost": 300
}
```

#### Example Response:
```json
{
    "DefectStatus": 1,
    "Confidence": 0.92
}
```

---

## Testing the API using Postman

Make sure the steps are executed in the correct order.

#### Uploading Dataset

- Open Postman.
- Create a `POST` request.
- Use the endpoint URL http://127.0.0.1:8000/upload.
- Go to the Body tab. 
- Select form-data.
- Add a key called file.
- In the value field, click the dropdown and select File.
- Upload dataset CSV file and hit send.

#### Training the model

- Set the request method to `POST`.
- Enter the endpoint URL: http://127.0.0.1:8000/train.
- No body or parameters are required for this endpoint. Hit send.

#### Getting predictions

- Set the request method to `POST`.
- Enter the endpoint URL: http://127.0.0.1:8000/predict.
- Click on the Body tab below the URL field.
- Select the raw option.
- Set the format to JSON.
- Enter the input data in the aforementioned input format then hit send to get the predictions.

---
 
