import mlflow
from src.common import load_config
c=load_config(); mlflow.set_tracking_uri(c["mlflow"]["tracking_uri"])
runs=mlflow.search_runs(experiment_names=[c["mlflow"]["experiment_name"]])
print(runs[["run_id","status","metrics.f1_score"]] if not runs.empty else "No runs found.")
