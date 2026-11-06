import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STEPS=["src/mlops_pipeline/01_load_data.py","src/mlops_pipeline/02_validate_data.py",
"src/mlops_pipeline/03_preprocessing.py","src/mlops_pipeline/04_validate_outputs.py",
"src/mlops_pipeline/05_train_registry.py","src/mlops_pipeline/06_model_evaluation.py",
"src/mlops_pipeline/07_quality_gate.py","src/mlops_pipeline/08_automate_lifecycle.py",
"src/mlops_pipeline/09_inference.py","src/mlops_pipeline/12_data_drift.py","src/mlops_pipeline/12_monitor_trigger.py"]
def main():
    for s in STEPS:
        print("\n[RUN]",s)
        r=subprocess.run([sys.executable,str(ROOT/s)],cwd=ROOT)
        if r.returncode: print("[STOP] Stage failed:",s); return False
    print("[SUCCESS] End-to-end SMS MLOps workflow completed."); return True
if __name__=="__main__": raise SystemExit(0 if main() else 1)
