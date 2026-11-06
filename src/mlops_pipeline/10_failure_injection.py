import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import json, shutil, subprocess, sys
from pathlib import Path
from src.common import load_config, project_path
def main():
    c=load_config(); raw=project_path(c["data"]["raw_path"]); backup=raw.with_suffix(".backup")
    if not raw.exists(): print("[ERROR] Dataset missing"); return False
    shutil.copy2(raw,backup); raw.unlink()
    try:
        result=subprocess.run([sys.executable,str(project_path("src/validate_data.py"))],cwd=project_path("."))
        passed=result.returncode != 0
    finally:
        shutil.move(backup,raw)
    report={"scenario":"missing_dataset","expected":"HALT","actual":"HALT" if passed else "CONTINUED","passed":passed}
    p=project_path(c["paths"]["failure_report"]); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report,indent=2))
    print("[SUCCESS] Failure injection check passed." if passed else "[ERROR] Failure injection failed.")
    return passed
if __name__=="__main__": raise SystemExit(0 if main() else 1)
