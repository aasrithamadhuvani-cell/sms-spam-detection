import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json
import pandas as pd
from scipy.stats import chi2_contingency
from src.common import load_config, project_path
def main():
    c=load_config(); col=c["data"]["text_column"]
    train=pd.read_csv(project_path(c["data"]["processed_dir"])/"train.csv")
    test=pd.read_csv(project_path(c["data"]["processed_dir"])/"test.csv")
    # Monitor token-length distribution as a lightweight text-feature drift proxy.
    a=train[col].astype(str).str.split().str.len(); b=test[col].astype(str).str.split().str.len()
    report={"baseline_mean_token_count":float(a.mean()),"current_mean_token_count":float(b.mean()),
            "absolute_mean_difference":float(abs(a.mean()-b.mean())),
            "note":"Text-length proxy only; compare production samples for operational drift."}
    p=project_path(c["paths"]["drift_report"]); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,indent=2)); print("[INFO] Drift proxy report:",report)
    return True
if __name__=="__main__": main()
