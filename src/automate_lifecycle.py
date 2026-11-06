import json
import mlflow
from mlflow import MlflowClient
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def main():
    cfg=load_config()
    mlflow.set_tracking_uri(cfg["mlflow"]["tracking_uri"])
    client=MlflowClient()
    name=cfg["registry"]["model_name"]
    versions=client.search_model_versions(f"name='{name}'")
    if not versions:
        print("[ERROR] No registered model versions. Run Lab 6 training first."); return False
    best=max(versions, key=lambda v: float(client.get_run(v.run_id).data.metrics.get(cfg["quality_gate"]["metric"],0)))
    metric=float(client.get_run(best.run_id).data.metrics.get(cfg["quality_gate"]["metric"],0))
    passed=metric >= float(cfg["quality_gate"]["minimum_value"])
    if passed:
        client.set_registered_model_alias(name, cfg["registry"]["alias"], best.version)
        decision="PROMOTED"
    else:
        decision="NOT_PROMOTED"
    report={"model_name":name,"selected_version":best.version,"metric":metric,"decision":decision}
    path=project_path(cfg["paths"]["lifecycle_report"]); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("[INFO] Model lifecycle:",decision, "metric=",round(metric,4))
    return passed
if __name__=="__main__":
    raise SystemExit(0 if main() else 1)
