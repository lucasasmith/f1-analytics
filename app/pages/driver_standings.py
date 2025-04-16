import duckdb
import polars as pl
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# 2025 Driver Standings")

standings_query = """
    select full_name, position, points
    from core.driver_standings order by position"""
standings_df = issue_query(query_str=standings_query, return_obj=Option.POLARS)
st.dataframe(standings_df)
