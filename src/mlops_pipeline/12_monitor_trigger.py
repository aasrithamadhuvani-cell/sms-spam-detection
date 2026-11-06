import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json, subprocess, sys
from src.common import load_config, project_path
def main():
    c=load_config(); report=project_path(c["paths"]["drift_report"])
    if not report.exists():
        r=subprocess.run([sys.executable,str(project_path("src/mlops_pipeline/12_data_drift.py"))],cwd=project_path("."))
        if r.returncode: return False
    data=json.loads(report.read_text())
    trigger=data["absolute_mean_difference"] > 2.0
    out={"retraining_triggered":trigger,"reason":"token-length distribution shift" if trigger else "within configured proxy threshold"}
    p=project_path("reports/monitor_trigger_report.json"); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2))
    print("[INFO] Monitoring trigger:",out); return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
