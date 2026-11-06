import json
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def evaluate():
    cfg = load_config()
    test = pd.read_csv(project_path(cfg["data"]["processed_dir"]) / "test.csv")
    model = joblib.load(project_path(cfg["paths"]["model"]))
    text_col = cfg["data"]["text_column"]
    y = test["target"].astype(int)
    pred = model.predict(test[text_col].astype(str))
    prob = model.predict_proba(test[text_col].astype(str))[:, 1]
    metrics = {
        "accuracy": float(accuracy_score(y, pred)),
        "precision": float(precision_score(y, pred, zero_division=0)),
        "recall": float(recall_score(y, pred, zero_division=0)),
        "f1_score": float(f1_score(y, pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y, prob))
    }
    report = {"stage":"SMS model evaluation", "test_rows":len(test), "metrics":metrics,
              "confusion_matrix":confusion_matrix(y,pred).tolist(),
              "classification_report":classification_report(y,pred,output_dict=True,zero_division=0)}
    out = project_path(cfg["paths"]["evaluation_report"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    errors = test.copy()
    errors["predicted"] = pred
    errors["probability_spam"] = prob
    errors[errors["target"] != errors["predicted"]].to_csv(project_path("outputs/misclassified_messages.csv"), index=False)
    print("[SUCCESS] Evaluation complete:", metrics)
    return report

if __name__ == "__main__":
    evaluate()
