import subprocess, sys
from pathlib import Path
def run():
    root=Path(__file__).resolve().parents[2]
    script=root/"src/mlops_pipeline/12_data_drift.py"
    return subprocess.run([sys.executable,str(script)],cwd=root).returncode==0
