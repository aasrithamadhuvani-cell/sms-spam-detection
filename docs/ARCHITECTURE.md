# Architecture

Raw SMS text → data validation → stratified split → TF-IDF + Logistic Regression → evaluation → MLflow tracking/registry → quality gate → champion alias → inference API → monitoring.

Unlike tabular churn prediction, the feature extractor is a text vectorizer. The saved scikit-learn Pipeline contains both TF-IDF and the classifier so training and inference use identical transformations.
