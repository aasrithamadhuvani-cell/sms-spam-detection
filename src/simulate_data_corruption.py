from pathlib import Path
import pandas as pd
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def main():
    cfg=load_config(); raw=project_path(cfg["data"]["raw_path"])
    if not raw.exists():
        print("[ERROR] Dataset missing. Run src/download_data.py first."); return False
    df=pd.read_csv(raw)
    df.loc[0,cfg["data"]["target_column"]]="unknown_label"
    out=project_path("data/monitoring/corrupted_sms.csv")
    out.parent.mkdir(parents=True,exist_ok=True); df.to_csv(out,index=False)
    print("[INFO] Corrupted test copy saved:",out)
    print("[INFO] Original raw dataset was not modified.")
    return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
