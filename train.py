"""Train a Random Forest on the Heart Disease dataset and save it with joblib.

Usage:  python train.py --data data/heart.csv
"""
import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

FEATURES = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
            "thalach", "exang", "oldpeak", "slope", "ca", "thal"]


def main(data_path: str, out_path: str) -> None:
    df = pd.read_csv(data_path).drop_duplicates()
    X, y = df[FEATURES], df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test accuracy: {acc:.3f}")
    print(classification_report(y_test, preds))

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, out)
    (out.parent / "metadata.json").write_text(
        json.dumps({"model_type": type(model).__name__,
                    "features": FEATURES,
                    "test_accuracy": round(acc, 4)}, indent=2)
    )
    print(f"Saved model to {out}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/heart.csv")
    p.add_argument("--out", default="model/heart_model.joblib")
    a = p.parse_args()
    main(a.data, a.out)
