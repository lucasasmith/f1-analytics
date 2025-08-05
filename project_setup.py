import logging
import subprocess
from pathlib import Path
from zipfile import ZipFile

import duckdb
import requests
from requests.exceptions import HTTPError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

TO_SECS = 10  # timeout seconds
RELEASES_URL = "https://api.github.com/repos/f1db/f1db/releases/latest"
F1_CSV_ASSET_NAME = "f1db-csv.zip"  # asset defined in the f1db releases.
DUCKDB_PATH = Path("f1.db")
DBT_PROJECT_PATH = "f1_dbt/"
DBT_SEED_PATH = "f1_dbt/seeds/"


def cleanup_existing() -> None:
    """Cleanup any existing db file."""
    if DUCKDB_PATH.exists():
        logger.info("Deleting existing DuckDB file for a clean project.")
        DUCKDB_PATH.unlink()


def setup_duckdb() -> None:
    """Bootstrap DuckDB."""
    logger.info("Creating DuckDB file and schemas.")
    with duckdb.connect(DUCKDB_PATH) as conn:
        conn.sql("create schema if not exists raw;")
        conn.sql("create schema if not exists core;")
        conn.sql("create schema if not exists reporting;")


def setup_dbt() -> None:
    """Run initial dbt commands and then build models."""
    logger.info("Setting up dbt and running models.")
    dbt_cmd_list = [
        ["dbt", "deps"],
        ["dbt", "seed"],
        ["dbt", "build", "--select", "core"],
        ["dbt", "build", "--select", "reporting"],
        ["dbt", "build", "--select", "marts"],
    ]

    for dbt_cmd in dbt_cmd_list:
        subprocess.run(dbt_cmd, cwd=DBT_PROJECT_PATH, check=True)


def get_data_files() -> None:
    """Download and extract files from GitHub release."""
    try:
        releases = requests.get(RELEASES_URL, timeout=TO_SECS)
        releases.raise_for_status()
        releases_json = releases.json()
    except HTTPError as exc:
        logger.exception("Failure getting /release/ URL.")
        raise HTTPError from exc
    else:
        for asset in releases_json["assets"]:
            if asset["name"] == F1_CSV_ASSET_NAME:
                csv_asset_url = asset["url"]

    # Download .zip file from GitHub.
    data_files_path = Path(f"{DBT_SEED_PATH}/csv_data.zip")
    logger.info(f"Downloading {F1_CSV_ASSET_NAME} @{csv_asset_url}")
    asset_data = requests.get(
        csv_asset_url, headers={"Accept": "application/octet-stream"}, timeout=TO_SECS
    )
    data_files_path.write_bytes(asset_data.content)

    # Extract all .csv files.
    logger.info(f"Extracting files from {data_files_path.name}")
    with ZipFile(data_files_path) as zf:
        zf.extractall(DBT_SEED_PATH)
    # Delete the .zip file.
    data_files_path.unlink()


def extract_data_files() -> None:
    # The extracted files use "-" which is incompatible with dbt.
    # Let's rename them and remove f1db- as well.
    seed_files = Path(DBT_SEED_PATH).glob("*.csv")
    for seed in seed_files:
        new_name = seed.name.replace("f1db-", "").replace("-", "_")
        new_path = DBT_SEED_PATH + new_name
        logger.info(f"Renaming {seed.name} to {new_path}")
        seed.rename(new_path)


if __name__ == "__main__":
    cleanup_existing()
    get_data_files()
    extract_data_files()
    setup_duckdb()
    setup_dbt()
