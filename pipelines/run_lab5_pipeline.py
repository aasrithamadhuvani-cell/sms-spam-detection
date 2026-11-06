import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.validate_data import validate
from src.preprocess_pipeline import preprocess
from src.validate_outputs import validate as validate_outputs
if __name__ == "__main__":
    if not validate(): raise SystemExit(1)
    preprocess()
    if not validate_outputs(): raise SystemExit(1)
    print("[SUCCESS] Lab 5 data pipeline completed.")
