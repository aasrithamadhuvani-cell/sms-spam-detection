import mlflow
from pathlib import Path
root=Path(__file__).resolve().parent
mlflow.set_tracking_uri(f"sqlite:///{(root/'artifacts'/'mlflow.db').as_posix()}")
print("MLflow version:",mlflow.__version__)
print("Tracking URI:",mlflow.get_tracking_uri())
