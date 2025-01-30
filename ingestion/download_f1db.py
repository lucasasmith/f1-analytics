import logging
from pathlib import Path
from zipfile import ZipFile

import requests
from requests.exceptions import HTTPError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

TO_SECS = 10  # timeout seconds
RELEASES_URL = "https://api.github.com/repos/f1db/f1db/releases/latest"
F1_CSV_ASSET_NAME = "f1db-csv.zip"  # asset defined in the f1db releases.
DOWNLOAD_PATH = "data_files"  # dir to create for the downloaded files.
DBT_SEED_PATH = "f1_analytics/seeds/"

try:
    releases = requests.get(RELEASES_URL, timeout=TO_SECS)
    releases.raise_for_status()
    releases_json = releases.json()
except HTTPError as exc:
    logger.exception("Failure getting /release/ URL.")
    raise HTTPError from exc
else:
    for asset in releases_json["assets"]:
        if asset["name"] == F1_CSV_ASSET_NAME:  # f1db-csv.zip is the name of the asset from GitHub.
            csv_asset_url = asset["url"]

# Create the dir and download .zip file from GitHub.
Path(DOWNLOAD_PATH).mkdir(exist_ok=True)
data_files_path = Path(f"{DOWNLOAD_PATH}/csv_data.zip")
logger.info(f"Downloading {F1_CSV_ASSET_NAME} @{csv_asset_url}")
asset_data = requests.get(
    csv_asset_url, headers={"Accept": "application/octet-stream"}, timeout=TO_SECS
)
data_files_path.write_bytes(asset_data.content)

# Extract all .csv files.
logger.info(f"Extracting files from {data_files_path.name}")
with ZipFile(data_files_path) as zf:
    zf.extractall(DBT_SEED_PATH)

# The extracted files use "-" which is incompatible with dbt.
# Let's rename them and remove f1db- as well.
seed_files = Path(DBT_SEED_PATH).glob("*.csv")
for seed in seed_files:
    new_name = seed.name.replace("f1db-", "").replace("-", "_")
    new_path = DBT_SEED_PATH + new_name
    logger.info(f"Renaming {seed.name} to {new_path}")
    seed.rename(new_path)
