import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
try:
    from src.common import load_config, project_path
except ModuleNotFoundError:
    from common import load_config, project_path

def train():
    cfg = load_config()
    base = project_path(cfg["data"]["processed_dir"])
    train_df = pd.read_csv(base / "train.csv")
    text_col = cfg["data"]["text_column"]
    model = Pipeline([
        ("tfidf", TfidfVectorizer(
            stop_words="english", max_features=cfg["model"]["max_features"],
            ngram_range=tuple(cfg["model"]["ngram_range"]), min_df=cfg["model"]["min_df"]
        )),
        ("classifier", LogisticRegression(
            max_iter=cfg["model"]["max_iter"], class_weight="balanced",
            random_state=cfg["project"]["random_state"]
        ))
    ])
    model.fit(train_df[text_col].astype(str), train_df["target"].astype(int))
    path = project_path(cfg["paths"]["model"])
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"[SUCCESS] Model trained and saved: {path}")
    return model

if __name__ == "__main__":
    train()
