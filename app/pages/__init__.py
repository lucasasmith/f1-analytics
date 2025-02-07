from enum import Enum

import duckdb

DUCKDB_FILE_PATH = "../f1_analytics/f1.db"


class Option(Enum):
    DATAFRAME = "DataFrame"
    PYTHON_OBJ = "PythonObject"
    POLARS = "PolarsDataFrame"


def issue_query(query_str: str, return_obj: Option):
    with duckdb.connect(DUCKDB_FILE_PATH, read_only=True) as conn:
        if return_obj == Option.DATAFRAME:
            return conn.sql(query_str).df()
        if return_obj == Option.PYTHON_OBJ:
            return conn.sql(query_str).fetchall()
        if return_obj == Option.POLARS:
            return conn.sql(query_str).pl()
        return None


def issue_query_params(query_str: str, return_obj: Option, query_params: list):
    with duckdb.connect(DUCKDB_FILE_PATH, read_only=True) as conn:
        if return_obj == Option.DATAFRAME:
            return conn.sql(query_str).df()
        if return_obj == Option.PYTHON_OBJ:
            return conn.sql(query_str, params=query_params).fetchall()
        return None
