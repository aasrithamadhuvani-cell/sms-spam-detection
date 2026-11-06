import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
steps=[
"src/download_data.py","src/mlops_pipeline/01_load_data.py",
"src/mlops_pipeline/02_validate_data.py","src/mlops_pipeline/03_preprocessing.py",
"src/mlops_pipeline/04_validate_outputs.py","src/mlops_pipeline/05_train_registry.py",
"src/mlops_pipeline/06_model_evaluation.py","src/mlops_pipeline/07_quality_gate.py",
"src/mlops_pipeline/08_automate_lifecycle.py","src/mlops_pipeline/09_inference.py",
"src/mlops_pipeline/12_monitor_trigger.py"
]
for step in steps:
    print("\n"+"="*70+"\nRUNNING "+step+"\n"+"="*70)
    result=subprocess.run([sys.executable,str(ROOT/step)],cwd=ROOT)
    if result.returncode:
        print("[ERROR] Pipeline stopped at",step); raise SystemExit(result.returncode)
print("[SUCCESS] All configured pipeline stages completed.")
