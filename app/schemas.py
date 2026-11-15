from pydantic import BaseModel, Field


class HeartInput(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Age in years")
    sex: int = Field(..., ge=0, le=1, description="1 = male, 0 = female")
    cp: int = Field(..., ge=0, le=3, description="Chest pain type (0-3)")
    trestbps: int = Field(..., ge=50, le=300, description="Resting blood pressure (mm Hg)")
    chol: int = Field(..., ge=50, le=700, description="Serum cholesterol (mg/dl)")
    fbs: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120 mg/dl")
    restecg: int = Field(..., ge=0, le=2, description="Resting ECG result (0-2)")
    thalach: int = Field(..., ge=50, le=250, description="Maximum heart rate achieved")
    exang: int = Field(..., ge=0, le=1, description="Exercise-induced angina")
    oldpeak: float = Field(..., ge=0, le=10, description="ST depression induced by exercise")
    slope: int = Field(..., ge=0, le=2, description="Slope of peak exercise ST segment")
    ca: int = Field(..., ge=0, le=4, description="Number of major vessels (0-4)")
    thal: int = Field(..., ge=0, le=3, description="Thalassemia code (0-3)")

    model_config = {
        "json_schema_extra": {
            "example": {"age": 58, "sex": 1, "cp": 0, "trestbps": 140, "chol": 240,
                        "fbs": 0, "restecg": 1, "thalach": 120, "exang": 1,
                        "oldpeak": 2.0, "slope": 1, "ca": 2, "thal": 3}
        }
    }


class PredictionOut(BaseModel):
    heart_disease: bool
    probability: float
