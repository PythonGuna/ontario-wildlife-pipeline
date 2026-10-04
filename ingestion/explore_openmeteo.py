import json
from pathlib import Path

import requests

URL = "https://archive-api.open-meteo.com/v1/archive"

# One test location (Toronto) and one month of daily data
params = {
    "latitude": 43.65,
    "longitude": -79.38,
    "start_date": "2025-05-01",
    "end_date": "2025-05-31",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Toronto",
}

resp = requests.get(URL, params=params, timeout=30)
resp.raise_for_status()
data = resp.json()

daily = data["daily"]
print("Top-level keys:", list(data.keys()))
print("Daily fields:", list(daily.keys()))
print("Days returned:", len(daily["time"]))
print("First 3 days:")
for i in range(3):
    print(
        daily["time"][i],
        daily["temperature_2m_max"][i],
        daily["temperature_2m_min"][i],
        daily["precipitation_sum"][i],
    )

# Save a sample next to the GBIF one
ROOT = Path(__file__).resolve().parent.parent
out_dir = ROOT / "docs"
out_dir.mkdir(exist_ok=True)
with open(out_dir / "openmeteo_sample.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved sample to", out_dir / "openmeteo_sample.json")