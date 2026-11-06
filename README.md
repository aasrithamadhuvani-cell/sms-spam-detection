# SMS Spam Detection — End-to-End MLOps Project

This project adapts the structure and workflow of the supplied Telco Churn MLOps project to a **text-classification** problem. It classifies SMS messages as `ham` (legitimate) or `spam`.

## Important dataset note
The raw UCI dataset is not embedded in this ZIP. Run `python src/download_data.py` once while connected to the internet. It downloads the public UCI SMS Spam Collection and creates `data/raw/spam.csv`. The source contains 5,574 labelled messages. Cite: Almeida & Hidalgo, *SMS Spam Collection*, UCI Machine Learning Repository, DOI: 10.24432/C5CC84.

## Setup (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/download_data.py
```

## Run all stages
Run commands from the project root (`sms_spam_detection`):
```powershell
python pipelines/run_lab3_baseline.py
python pipelines/run_lab4_tracking.py
python pipelines/run_lab5_pipeline.py
python pipelines/run_lab6_registry.py
python src/mlops_pipeline/07_quality_gate.py
python src/mlops_pipeline/08_automate_lifecycle.py
python src/mlops_pipeline/09_inference.py
python src/mlops_pipeline/10_failure_injection.py
python src/mlops_pipeline/11_prepare_deployment.py
```

Or run the complete workflow:
```powershell
python pipelines/run_all_labs.py
```

## Labs mapped to the Churn project
- Labs 3–4: baseline text classifier, evaluation, MLflow experiment tracking and reproducibility.
- Lab 5: input schema/data validation, TF-IDF preprocessing, output validation.
- Lab 6: model registration and lifecycle automation.
- Lab 7: end-to-end configurable pipeline.
- Lab 8: CI workflow and automated tests.
- Lab 9: failure injection, validation and recovery checks.
- Lab 10: FastAPI model serving, input validation and inference logging.
- Lab 11: Docker image and Kubernetes deployment templates.
- Lab 12: data/prediction drift and performance monitoring, retraining trigger.
- Lab 13: end-to-end runner and monitoring workflow.

## API
After the model is trained and assigned the MLflow `champion` alias:
```powershell
uvicorn api.main:app --reload
```
Open `http://127.0.0.1:8000/docs`. POST `/predict` with:
```json
{"message":"Congratulations! You have won a free prize. Reply now"}
```

## Reproducibility
The train/test split uses a fixed random seed. TF-IDF is fitted on training messages only. Metrics include accuracy, precision, recall, F1 and ROC-AUC. Never claim a run passed until you execute it and inspect the generated reports.
