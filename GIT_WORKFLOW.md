# Git workflow evidence checklist
```bash
git init
git add .
git commit -m "Initial SMS spam MLOps project"
git branch feature/data-validation
git checkout feature/data-validation
git add .
git commit -m "Add data validation"
git checkout main
git merge feature/data-validation
git tag -a v1.0 -m "SMS spam baseline"
git log --oneline --graph --decorate --all
```
Capture your actual Git history; do not fabricate evidence.
