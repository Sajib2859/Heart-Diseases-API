# Heart Disease Prediction API

A FastAPI app that predicts the presence of heart disease from patient data, using a Random Forest model trained on the [Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset). It is packaged with Docker and deployed on Render.

**Live app:** https://heart-diseases-api-j92y.onrender.com
**API docs:** https://heart-diseases-api-j92y.onrender.com/docs

## Project structure

```
app/                 FastAPI code (main.py, schemas.py)
model/               trained model (heart_model.joblib)
data/                heart.csv
train.py             trains and saves the model
Dockerfile
docker-compose.yml
requirements.txt
```

## Run with Docker

```bash
docker-compose build
docker-compose up
```

Then open http://localhost:8000/docs

## Train the model

```bash
pip install -r requirements.txt
python train.py --data data/heart.csv
```

The model is saved to `model/heart_model.joblib`. Python 3.11 is recommended.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | health check |
| GET | `/info` | model type and feature list |
| POST | `/predict` | returns `heart_disease` (true/false) and probability |

## Example

```bash
curl -X POST https://heart-diseases-api-j92y.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"age":58,"sex":1,"cp":0,"trestbps":140,"chol":240,"fbs":0,"restecg":1,"thalach":120,"exang":1,"oldpeak":2.0,"slope":1,"ca":2,"thal":3}'
```

Response:

```json
{"heart_disease": false, "probability": 0.005}
```

## Deployment

Deployed on Render as a Docker web service, built directly from this repository.