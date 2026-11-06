import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from pathlib import Path
from src.common import project_path
def main():
    p=project_path("logs/inference.jsonl")
    count=sum(1 for line in p.open(encoding="utf-8") if line.strip()) if p.exists() else 0
    print(f"[INFO] Logged inference requests: {count}")
    return count
if __name__=="__main__": main()
