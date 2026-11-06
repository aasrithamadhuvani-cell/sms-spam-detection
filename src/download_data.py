from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "spam.csv"
URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        print(f"[INFO] Dataset already exists: {OUT}")
        return
    print("[INFO] Downloading the UCI SMS Spam Collection...")
    with urlopen(URL, timeout=60) as response:
        archive = ZipFile(BytesIO(response.read()))
    with archive.open("SMSSpamCollection") as file:
        df = pd.read_csv(file, sep="\t", header=None, names=["label", "message"], encoding="latin-1")
    df.to_csv(OUT, index=False)
    print(f"[SUCCESS] Saved {len(df)} rows to {OUT}")

if __name__ == "__main__":
    main()
