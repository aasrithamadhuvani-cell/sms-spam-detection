import mlflow
from mlflow import MlflowClient
from src.common import load_config
c=load_config(); mlflow.set_tracking_uri(c["mlflow"]["tracking_uri"])
client=MlflowClient()
for version in client.search_model_versions(f"name='{c['registry']['model_name']}'"):
    print("version=",version.version,"stage=",version.current_stage,"run_id=",version.run_id)
