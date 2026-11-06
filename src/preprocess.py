import json
import pandas as pd
from sklearn.model_selection import train_test_split
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def preprocess():
    cfg = load_config()
    raw = pd.read_csv(project_path(cfg["data"]["raw_path"]))
    text_col, target_col = cfg["data"]["text_column"], cfg["data"]["target_column"]
    df = raw[[text_col, target_col]].dropna().drop_duplicates().copy()
    df[text_col] = df[text_col].astype(str).str.strip()
    df[target_col] = df[target_col].astype(str).str.lower().str.strip()
    df = df[df[text_col].str.len() > 0]
    df["target"] = (df[target_col] == "spam").astype(int)
    train, test = train_test_split(
        df, test_size=cfg["data"]["test_size"], random_state=cfg["project"]["random_state"],
        stratify=df["target"]
    )
    out = project_path(cfg["data"]["processed_dir"])
    out.mkdir(parents=True, exist_ok=True)
    train[[text_col, "target"]].to_csv(out / "train.csv", index=False)
    test[[text_col, "target"]].to_csv(out / "test.csv", index=False)
    meta = {
        "rows_after_cleaning": int(len(df)), "train_rows": int(len(train)),
        "test_rows": int(len(test)), "label_mapping": {"ham": 0, "spam": 1},
        "random_state": cfg["project"]["random_state"], "test_size": cfg["data"]["test_size"],
        "text_column": text_col
    }
    (out / "dataset_metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"[SUCCESS] Preprocessing complete. train={len(train)}, test={len(test)}")
    return True

if __name__ == "__main__":
    preprocess()
