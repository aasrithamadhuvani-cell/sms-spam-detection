from pathlib import Path
import shutil
import joblib
from src.common import load_config, project_path

def main():
    cfg=load_config()
    source=project_path(cfg["paths"]["model"])
    if not source.exists():
        print("[ERROR] Train the model before preparing local deployment.")
        return False
    dest=project_path("deployment/model.pkl")
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,dest)
    check=joblib.load(dest)
    print("[SUCCESS] Local deployment model verified:",type(check).__name__)
    return True
if __name__=="__main__":
    raise SystemExit(0 if main() else 1)
