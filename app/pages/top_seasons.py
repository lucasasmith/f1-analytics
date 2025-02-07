import duckdb
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# F1 Top Seasons in History")

st.markdown("### Top 100 Seasons in F1 History")
top_seasons_query = "from reporting.top_seasons_all_time"
top_seasons_df = issue_query(query_str=top_seasons_query, return_obj=Option.DATAFRAME)
st.dataframe(top_seasons_df, hide_index=True, use_container_width=True)
