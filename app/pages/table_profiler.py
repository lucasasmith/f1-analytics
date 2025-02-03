import duckdb
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# Table Profiler")


schema_selection = st.selectbox(label="Choose schema", options=["raw", "core"])
table_list_query = (
    f"select table_name from information_schema.tables where table_schema = '{schema_selection}';"
)
table_list = issue_query(table_list_query, return_obj=Option.PYTHONOBJ)
tables = (table[0] for table in table_list)
table_selection = st.selectbox(label="Table", options=tables)
