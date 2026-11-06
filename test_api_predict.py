import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from api.main import predict, loader
from api.schemas import SMSRequest

loader.load()
print("[INFO] Model ready:", loader.ready())

sample1 = SMSRequest(message="Congratulations! You have won a $1000 Walmart gift card. Click here now.")
res1 = predict(sample1)
print("[TEST PREDICT SPAM]:", res1)

sample2 = SMSRequest(message="Hey are you free for lunch tomorrow at 1pm?")
res2 = predict(sample2)
print("[TEST PREDICT HAM]:", res2)

assert res1["prediction"] == "spam"
assert res2["prediction"] == "ham"
print("[SUCCESS] API prediction and logging verified successfully!")
