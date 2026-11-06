import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.validate_data import validate
from src.preprocess import preprocess
from src.train import train
from src.evaluate import evaluate
if __name__ == "__main__":
    if not validate(): raise SystemExit(1)
    preprocess(); train(); evaluate()
    print("[SUCCESS] Lab 3 baseline pipeline completed.")
