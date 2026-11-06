import sys
import pandas as pd
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def validate():
    cfg=load_config(); d=project_path(cfg["data"]["processed_dir"])
    for name in ["train.csv","test.csv","dataset_metadata.json"]:
        if not (d/name).exists():
            print("[ERROR] Missing processed output:", name); return False
    for name in ["train.csv","test.csv"]:
        df=pd.read_csv(d/name)
        if df.empty or df.isna().any().any() or not set(df.target.unique()).issubset({0,1}):
            print("[ERROR] Invalid processed file:",name); return False
    print("[SUCCESS] Processed output validation PASSED.")
    return True
if __name__=="__main__": sys.exit(0 if validate() else 1)
