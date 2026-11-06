import os
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def run():
    cfg = load_config()
    uri = os.getenv("MLFLOW_TRACKING_URI") or cfg["mlflow"]["tracking_uri"]
    mlflow.set_tracking_uri(uri)
    mlflow.set_experiment(cfg["mlflow"]["experiment_name"])
    train = pd.read_csv(project_path(cfg["data"]["processed_dir"]) / "train.csv")
    test = pd.read_csv(project_path(cfg["data"]["processed_dir"]) / "test.csv")
    col = cfg["data"]["text_column"]
    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", max_features=cfg["model"]["max_features"],
                                  ngram_range=tuple(cfg["model"]["ngram_range"]), min_df=cfg["model"]["min_df"])),
        ("classifier", LogisticRegression(max_iter=cfg["model"]["max_iter"], class_weight="balanced",
                                           random_state=cfg["project"]["random_state"]))
    ])
    with mlflow.start_run() as run:
        model.fit(train[col].astype(str), train["target"].astype(int))
        pred = model.predict(test[col].astype(str))
        prob = model.predict_proba(test[col].astype(str))[:, 1]
        metrics = {
            "accuracy": accuracy_score(test["target"], pred),
            "precision": precision_score(test["target"], pred, zero_division=0),
            "recall": recall_score(test["target"], pred, zero_division=0),
            "f1_score": f1_score(test["target"], pred, zero_division=0),
            "roc_auc": roc_auc_score(test["target"], prob)
        }
        mlflow.log_params({"classifier":"LogisticRegression", "max_features":cfg["model"]["max_features"],
                           "ngram_range":str(cfg["model"]["ngram_range"]), "random_state":cfg["project"]["random_state"]})
        mlflow.log_metrics({k:float(v) for k,v in metrics.items()})
        mlflow.sklearn.log_model(model, "sms_pipeline", registered_model_name=cfg["registry"]["model_name"], pip_requirements=["scikit-learn", "pandas"])
        print("[SUCCESS] MLflow run:", run.info.run_id, metrics)
        return metrics

if __name__ == "__main__":
    run()
