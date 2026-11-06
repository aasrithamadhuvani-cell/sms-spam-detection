import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json
import mlflow, pandas as pd
from src.common import load_config, project_path
def main():
    c=load_config(); mlflow.set_tracking_uri(c["mlflow"]["tracking_uri"])
    uri=f"models:/{c['registry']['model_name']}@{c['registry']['alias']}"
    try: model=mlflow.pyfunc.load_model(uri)
    except Exception as e: print("[ERROR] Champion model unavailable:",e); return False
    raw=pd.read_csv(project_path(c["data"]["raw_path"]))
    col=c["data"]["text_column"]; sample=raw.sample(min(10,len(raw)),random_state=7).copy()
    sample["prediction"]=model.predict(sample[col].astype(str))
    sample["predicted_label"]=sample["prediction"].map({0:"ham",1:"spam"})
    out=project_path(c["paths"]["inference_output"]); out.parent.mkdir(parents=True,exist_ok=True)
    sample.to_csv(out,index=False); print("[SUCCESS] Inference output:",out); return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
