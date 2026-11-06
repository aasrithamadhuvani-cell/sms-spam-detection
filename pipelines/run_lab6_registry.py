import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.validate_data import validate
from src.preprocess import preprocess
from src.train_registry import run
from src.automate_lifecycle import main
if __name__ == "__main__":
    if not validate(): raise SystemExit(1)
    preprocess(); run()
    print("[INFO] Run lifecycle promotion after checking quality gate.")
    print("[SUCCESS] Lab 6 model registry training completed.")
