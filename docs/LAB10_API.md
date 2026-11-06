# Lab 10 — Model Serving API
FastAPI exposes `/`, `/health`, `/metadata`, and `/predict`. The request contains one `message` string. The response contains `ham` or `spam` and a spam probability. Inference events are appended to `logs/inference.jsonl`.
