from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from app.schemas import HeartInput, PredictionOut

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "heart_model.joblib"
FEATURES = list(HeartInput.model_fields.keys())
state: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    state["model"] = joblib.load(MODEL_PATH)
    yield
    state.clear()


app = FastAPI(title="Heart Disease Prediction API", version="1.0.0", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": "model" in state}


@app.get("/info")
def info():
    model = state.get("model")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {
        "model_type": type(model).__name__,
        "n_features": len(FEATURES),
        "features": FEATURES,
        "target": "heart_disease (True = presence, False = absence)",
    }


@app.post("/predict", response_model=PredictionOut)
def predict(payload: HeartInput):
    model = state.get("model")
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    X = pd.DataFrame([payload.model_dump()], columns=FEATURES)
    proba = float(model.predict_proba(X)[0][1])
    return PredictionOut(heart_disease=proba >= 0.5, probability=round(proba, 4))
