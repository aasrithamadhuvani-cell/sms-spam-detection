import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
def run():
    from src.mlops_pipeline import _drift_proxy_impl
    return _drift_proxy_impl.run()
