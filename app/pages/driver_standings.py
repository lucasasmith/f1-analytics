import duckdb
import polars as pl
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# 2025 Driver Standings")

col1, col2, col3 = st.columns(3)

with col1:
    standings_query = """
        select full_name, position, points
        from core.driver_standings order by position"""
    standings_df = issue_query(query_str=standings_query, return_obj=Option.POLARS)
    st.text("2025 Standings:")
    st.dataframe(standings_df)

with col2:
    results_query = "from reporting.race_results_2025"
    results_df = issue_query(query_str=results_query, return_obj=Option.POLARS)
    st.text("Result by race:")
    st.dataframe(results_df.sort("race_desc", "position"))

st.text("Result by race:")
st.line_chart(data=results_df, x="race_desc", y="position", color="driver_id", height=800)
