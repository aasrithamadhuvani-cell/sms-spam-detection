import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.validate_data import validate
from src.preprocess import preprocess
from src.train_mlflow import run
from src.validate_reproducibility import main
if __name__ == "__main__":
    if not validate(): raise SystemExit(1)
    preprocess(); run()
    if not main(): raise SystemExit(1)
    print("[SUCCESS] Lab 4 MLflow tracking completed.")
