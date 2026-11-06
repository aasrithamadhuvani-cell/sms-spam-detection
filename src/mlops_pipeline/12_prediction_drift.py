import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json
from pathlib import Path
from src.common import project_path
def main():
    log=project_path("logs/inference.jsonl")
    if not log.exists():
        print("[INFO] No inference records yet; prediction drift is not measurable.")
        return True
    records=[json.loads(line) for line in log.read_text(encoding="utf-8").splitlines() if line.strip()]
    labels=[r.get("prediction") for r in records if r.get("prediction")]
    report={"inference_records":len(records),"spam_prediction_rate":(labels.count("spam")/len(labels) if labels else None)}
    p=project_path("reports/prediction_drift_report.json"); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,indent=2)); print("[INFO] Prediction drift summary:",report); return True
if __name__=="__main__": main()
