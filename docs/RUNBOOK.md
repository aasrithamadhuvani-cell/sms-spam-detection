# Runbook
1. Activate `.venv` and install `requirements.txt`.
2. Download UCI data using `python src/download_data.py`.
3. Run Lab 3 baseline.
4. Run Lab 4 MLflow tracking.
5. Run Lab 5 validation and Lab 6 registry training.
6. Inspect `reports/evaluation_report.json` and the quality gate.
7. Promote a model alias only after quality checks.
8. Start API with `uvicorn api.main:app --reload`.
9. Inspect `logs/inference.jsonl`, drift report and monitoring trigger report.
