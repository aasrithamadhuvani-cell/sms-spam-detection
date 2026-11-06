# MLflow and CI Setup
Default tracking URI: `sqlite:///artifacts/mlflow.db`. MLflow stores experiment runs locally. Registered model name is `SMS_Spam_Production_Model`; lifecycle automation assigns the `champion` alias when the configured F1 quality gate passes. In CI, use a temporary local tracking database.
