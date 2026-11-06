from pathlib import Path
import joblib
try:
    import mlflow
except ImportError:
    mlflow = None

class ModelLoader:
    def __init__(self):
        self.model=None
        self.model_uri=None
    def load(self):
        root=Path(__file__).resolve().parents[1]
        local=root/"deployment"/"model.pkl"
        if not local.exists():
            local=root/"models"/"sms_spam_pipeline.pkl"
        if local.exists():
            self.model=joblib.load(local)
            self.model_uri="models:/SMS_Spam_Production_Model@champion"
            print("[SUCCESS] Loaded model bundle (champion).")
            return
        if mlflow is not None:
            mlflow.set_tracking_uri(f"sqlite:///{(root/'artifacts'/'mlflow.db').as_posix()}")
            try:
                self.model_uri="models:/SMS_Spam_Production_Model@champion"
                self.model=mlflow.sklearn.load_model(self.model_uri)
                print("[SUCCESS] Loaded MLflow champion model.")
            except Exception as exc:
                print("[WARNING] No trained model available:",exc)
    def ready(self): return self.model is not None
