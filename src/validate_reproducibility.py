import json
from pathlib import Path
try:
    from src.common import load_config, project_path
    from src.train_mlflow import run
except ModuleNotFoundError:
    from common import load_config, project_path
    from train_mlflow import run

def main():
    first = run()
    second = run()
    keys = ["accuracy", "precision", "recall", "f1_score", "roc_auc"]
    passed = all(abs(first[k] - second[k]) < 1e-12 for k in keys)
    report = {"stage":"reproducibility", "first_run":first, "second_run":second,
              "status":"PASS" if passed else "FAIL"}
    path = project_path("reports/reproducibility_report.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("[SUCCESS] Reproducibility validation:", report["status"])
    return passed

if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
