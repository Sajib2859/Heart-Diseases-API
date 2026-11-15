# Heart Disease Prediction API

FastAPI service that serves a Random Forest classifier trained on the
[Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).
Containerised with Docker and deployed on Render.

**Live URL:** `https://<your-service>.onrender.com`  (docs at `/docs`)

## Project structure
```
app/            FastAPI application (main.py, schemas.py)
model/          Trained model (heart_model.joblib) + metadata.json
data/           Place heart.csv here for training (not needed to run the API)
train.py        Training script
Dockerfile
docker-compose.yml
requirements.txt
```

## Train the model (optional; a trained model is already committed)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python train.py --data data/heart.csv
```

## Run with Docker
```bash
docker-compose build
docker-compose up
```
Swagger UI: http://localhost:8000/docs

## Endpoints
| Method | Path       | Description                                |
|--------|------------|--------------------------------------------|
| GET    | `/health`  | Liveness check                             |
| GET    | `/info`    | Model type and feature list                |
| POST   | `/predict` | Returns `heart_disease` (true/false) + probability |

## Example
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":58,"sex":1,"cp":0,"trestbps":140,"chol":240,"fbs":0,"restecg":1,"thalach":120,"exang":1,"oldpeak":2.0,"slope":1,"ca":2,"thal":3}'
```

## Deploy on Render
1. Push this repository to GitHub.
2. Render dashboard -> New -> Web Service -> connect the repo.
3. Language: **Docker**; root directory blank (Dockerfile at root).
4. Create the service; set Health Check Path to `/health`.

> Disclaimer: educational project; not a medical device.
