import duckdb
import streamlit as st

st.set_page_config(layout="wide")
st.markdown("# F1 Top Seasons in History")


def issue_query(query_str: str):
    with duckdb.connect("../f1_analytics/f1.db") as conn:
        return conn.sql(query_str).df()


st.markdown("### Top 100 Seasons in F1 History")
top_seasons_query = "select * from reporting.top_seasons_all_time"
top_seasons_df = issue_query(top_seasons_query)
st.dataframe(top_seasons_df, hide_index=True, use_container_width=True)
