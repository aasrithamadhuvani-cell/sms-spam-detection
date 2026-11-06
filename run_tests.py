import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

print("[TEST 1] Testing validation functions...")
from tests.test_validation import test_validation_function_exists
test_validation_function_exists()
print("-> PASSED")

print("[TEST 2] Testing Dockerfile and API presence...")
from tests.test_local_vs_container import test_dockerfile_exists
test_dockerfile_exists()
print("-> PASSED")

print("[TEST 3] Testing text pipeline latency...")
from tests.test_performance import test_text_pipeline_smoke_latency
test_text_pipeline_smoke_latency()
print("-> PASSED")

print("[TEST 4] Testing API root & health endpoints...")
from api.main import root, health
r1 = root()
assert r1["status"] == "success"
r2 = health()
assert r2["status"] == "healthy"
print("-> PASSED:", r1, r2)

print("\n" + "=" * 50)
print("[SUCCESS] All 4 test suites passed successfully!")
print("=" * 50)
