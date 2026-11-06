import sys
import pandas as pd
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def validate():
    cfg = load_config()
    path = project_path(cfg["data"]["raw_path"])
    if not path.exists():
        print(f"[ERROR] Dataset missing: {path}. Run python src/download_data.py")
        return False
    df = pd.read_csv(path)
    required = {cfg["data"]["text_column"], cfg["data"]["target_column"]}
    missing = required - set(df.columns)
    if missing:
        print(f"[ERROR] Missing columns: {sorted(missing)}")
        return False
    if df.empty or df[list(required)].isna().any().any():
        print("[ERROR] Dataset is empty or required fields contain missing values.")
        return False
    labels = set(df[cfg["data"]["target_column"]].astype(str).str.lower().unique())
    if not labels.issubset({"ham", "spam"}):
        print(f"[ERROR] Unexpected labels: {labels}")
        return False
    if not df[cfg["data"]["text_column"]].map(lambda x: isinstance(x, str)).all():
        print("[ERROR] Message column must contain text.")
        return False
    print(f"[SUCCESS] Data validation PASSED. Rows={len(df)}, labels={labels}")
    return True

if __name__ == "__main__":
    sys.exit(0 if validate() else 1)
