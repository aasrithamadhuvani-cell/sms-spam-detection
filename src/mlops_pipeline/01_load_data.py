import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from pathlib import Path
import pandas as pd
from src.common import load_config, project_path
def main():
    cfg=load_config(); p=project_path(cfg["data"]["raw_path"])
    if not p.exists():
        print("[ERROR] Dataset missing. Run python src/download_data.py"); return False
    df=pd.read_csv(p); print("[INFO] SMS dataset shape:",df.shape); print(df.head())
    return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
