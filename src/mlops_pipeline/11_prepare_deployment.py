import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json, shutil, joblib, mlflow
from pathlib import Path
from src.common import load_config, project_path
def main():
    c=load_config(); mlflow.set_tracking_uri(c["mlflow"]["tracking_uri"])
    uri=f"models:/{c['registry']['model_name']}@{c['registry']['alias']}"
    try: model=mlflow.sklearn.load_model(uri)
    except Exception as e: print("[ERROR] Champion model unavailable:",e); return False
    d=project_path("deployment"); d.mkdir(parents=True,exist_ok=True)
    joblib.dump(model,d/"model.pkl")
    meta={"model_name":c["registry"]["model_name"],"model_uri":uri,"stage":"champion alias"}
    (d/"model_metadata.json").write_text(json.dumps(meta,indent=2))
    print("[SUCCESS] Deployment bundle prepared."); return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
