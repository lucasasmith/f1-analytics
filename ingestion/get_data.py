import logging
import shutil
from pathlib import Path

import kagglehub
from dotenv import load_dotenv
from rich.logging import RichHandler

load_dotenv()
FORMAT = "%(message)s"
logging.basicConfig(level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])
logger = logging.getLogger("rich")

# NOTE: Kaggle login details should be stored in a .env file and are read using dotenv.
logger.info("Starting download from Kaggle.")
dl_path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

# Check if a data folder exists and create it if not
target_dir = Path().cwd().joinpath("f1_analytics/seeds/f1")
if not target_dir.exists():
    target_dir.mkdir()
    logger.info(f"{target_dir} created")


# Find downloaded csv file and copy them to this dir.
source_csv_files = Path(dl_path).glob("**/*.csv")
for file in source_csv_files:
    logger.info(f"Copying {file} to {target_dir}.")
    shutil.copy(file, target_dir)
