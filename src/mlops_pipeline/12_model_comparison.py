import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json
from pathlib import Path
from src.common import project_path
def main():
    p=project_path("reports/evaluation_report.json")
    if not p.exists():
        print("[ERROR] Run evaluation first."); return False
    data=json.loads(p.read_text())
    print("[INFO] Current registered candidate metrics:")
    for k,v in data["metrics"].items(): print(f"{k}: {v:.4f}")
    return True
if __name__=="__main__": main()
