## Project
This is a project to demonstrate an ELT process to ingest, model, transform, and analyze Formula 1 data. Every tool used is open to use and no signups/logins required. Tools utilized:
- DuckDB
- dbt
- Streamlit

Architecture
![Alt text](https://github.com/lucasasmith/f1-analytics/blob/main/assets/f1_diagram.png)


## Setup
- NOTE: the following most likely only works on macos.
- Clone repo.
- Create a new venv with `uv`.
  - `uv venv --python 3.13` and activate.
- Install requirements `uv pip install -r requirements.txt`.
- Run `project_setup.py`. This will:
  - Download a .zip of csv files from the [f1db](https://github.com/f1db/f1db) repo latest release.
  - Place the .csv files in the dbt `seeds` dir and rename them appropriately.
  - Create and setup a DuckDB `f1.db` file and create `raw`, `core`, and `reporting` schemas.
  - Run `dbt deps`, `dbt seed`, and build the `core` and `reporting` models.
  - Warn about any `data_tests` that have failed.
  - This script can also be used to completely refresh the db file and re-run models.

## Next Steps
As of now, next steps to work with the data are:
- Add more dbt models
- Navigate to the `app` dir and run `streamlit run main_page.py`. This will open a Streamlit app where ad-hoc queries can be issued and some pre-built analysis has been completed.
![Alt text](https://github.com/lucasasmith/f1-analytics/blob/main/assets/streamlit_demo.png)

### Source Data
Credit to [f1db](https://github.com/f1db/f1db) for the source data of this project. Thanks!
