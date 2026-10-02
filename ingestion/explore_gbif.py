import json
import requests
from pathlib import Path

URL = "https://api.gbif.org/v1/occurrence/search"

params = {
    "country": "CA",
    "stateProvince": "Ontario",
    "year": "2025",
    "hasCoordinate": "true",
    "limit": 20,
}

resp = requests.get(URL, params=params, timeout=30)
resp.raise_for_status()
data = resp.json()

print("Total matching records:", data["count"])
print("Fields in one record:", len(data["results"][0]))
print(json.dumps(data["results"][0], indent=2)[:3000])

ROOT = Path(__file__).resolve().parent.parent
out_dir = ROOT / "docs"
out_dir.mkdir(exist_ok=True)

with open(out_dir / "gbif_sample.json", "w") as f:
    json.dump(data["results"], f, indent=2)

print("Saved sample to", out_dir / "gbif_sample.json")
