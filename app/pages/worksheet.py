import duckdb
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# Query Worksheet")


query_str = st.text_area("Enter a DuckDB query here.", height=300)
if st.button("Run"):
    data_return = issue_query(query_str=query_str, return_obj=Option.DATAFRAME)
    st.dataframe(data_return, hide_index=True, use_container_width=True)
