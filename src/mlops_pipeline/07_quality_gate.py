import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json, sys
from src.common import load_config, project_path
def main():
    c=load_config(); p=project_path(c["paths"]["evaluation_report"])
    if not p.exists(): print("[ERROR] Evaluation report missing"); return False
    report=json.loads(p.read_text(encoding="utf-8"))
    metric=c["quality_gate"]["metric"]; minimum=float(c["quality_gate"]["minimum_value"])
    actual=float(report["metrics"][metric]); passed=actual>=minimum
    out={"metric":metric,"minimum_value":minimum,"actual_value":actual,"status":"PASSED" if passed else "FAILED"}
    dest=project_path(c["paths"]["quality_gate_report"]); dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print("[INFO] Quality gate:",out["status"],f"({actual:.4f} >= {minimum:.4f})")
    return passed
if __name__=="__main__": raise SystemExit(0 if main() else 1)
