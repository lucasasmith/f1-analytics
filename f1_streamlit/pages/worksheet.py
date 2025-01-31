import duckdb
import streamlit as st

DUCKDB_FILE_PATH = "../f1_analytics/f1.db"

st.set_page_config(layout="wide")
st.markdown("# Query Worksheet")


def issue_query(query_str: str):
    with duckdb.connect(DUCKDB_FILE_PATH) as conn:
        return conn.sql(query_str).df()


query_str = st.text_area("Enter a DuckDB query here.", height=300)
if st.button("Run"):
    data_return = issue_query(query_str)
    st.dataframe(data_return)
st.markdown(f"Database file path: {DUCKDB_FILE_PATH}")
