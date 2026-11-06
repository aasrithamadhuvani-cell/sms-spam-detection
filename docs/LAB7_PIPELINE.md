# Lab 7 — Configurable End-to-End Pipeline
The pipeline reads paths, random seed, TF-IDF settings, model parameters and quality thresholds from `config.yaml`. Run `python src/mlops_pipeline/13_end_to_end.py`. Every stage returns a non-zero exit code on failure so later stages do not run after a failed prerequisite.
