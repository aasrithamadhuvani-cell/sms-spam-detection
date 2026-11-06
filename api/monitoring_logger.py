import json
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def log_event(record):
    path=ROOT/"logs"/"inference.jsonl"; path.parent.mkdir(parents=True,exist_ok=True)
    record["timestamp"]=datetime.now(timezone.utc).isoformat()
    with path.open("a",encoding="utf-8") as f: f.write(json.dumps(record)+"\n")
