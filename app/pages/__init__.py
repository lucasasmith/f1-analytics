from enum import Enum

import duckdb


class Option(Enum):
    DATAFRAME = "DataFrame"
    PYTHONOBJ = "PythonObject"


def issue_query(query_str: str, return_obj: Option):
    with duckdb.connect("../f1_analytics/f1.db") as conn:
        if return_obj == Option.DATAFRAME:
            return conn.sql(query_str).df()
        if return_obj == Option.PYTHONOBJ:
            return conn.sql(query_str).fetchall()
        return None
