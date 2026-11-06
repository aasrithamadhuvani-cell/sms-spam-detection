import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json, time
from pathlib import Path
import joblib, pandas as pd
from src.common import load_config, project_path

def main():
    c=load_config(); model_path=project_path(c["paths"]["model"])
    test_path=project_path(c["data"]["processed_dir"])/"test.csv"
    if not model_path.exists() or not test_path.exists():
        print("[ERROR] Train model and preprocess data first."); return False
    model=joblib.load(model_path); df=pd.read_csv(test_path)
    col=c["data"]["text_column"]; sample=df.head(min(100,len(df)))
    start=time.perf_counter(); model.predict(sample[col].astype(str))
    elapsed=(time.perf_counter()-start)*1000/max(len(sample),1)
    report={"sample_count":len(sample),"avg_latency_ms_per_message":elapsed}
    p=project_path("reports/performance_report.json"); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,indent=2)); print("[INFO] Performance report:",report); return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
