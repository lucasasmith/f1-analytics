import duckdb
import streamlit as st

from pages import Option, issue_query, issue_query_params

st.set_page_config(layout="wide")
st.markdown("# Table Profiler")


schema_selection = st.selectbox(label="Choose schema", options=["raw", "core"])
table_list_query = "select table_name from information_schema.tables where table_schema = $1;"
table_list = issue_query_params(
    query_str=table_list_query, query_params=[schema_selection], return_obj=Option.PYTHON_OBJ
)
tables = (table[0] for table in table_list)
table_selection = st.selectbox(label="Table", options=tables)
fqn = f"{schema_selection}.{table_selection}"

# Show table summary.
if st.button(f"Summarize table {fqn}"):
    table_summary_query = f"summarize {fqn};"
    table_summary_df = issue_query(query_str=table_summary_query, return_obj=Option.DATAFRAME)
    st.dataframe(table_summary_df)
    st.text("Table preview")
    table_preview_query = f"select * from {fqn} limit 5000"
    table_preview_df = issue_query(query_str=table_preview_query, return_obj=Option.POLARS)
    st.dataframe(table_preview_df)
