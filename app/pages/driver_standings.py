import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# 2025 Driver Standings")

col1, col2 = st.columns(2)

with col1:
    standings_query = """
        select driver_id, position, points
        from core.driver_standings order by position"""
    standings_df = issue_query(query_str=standings_query, return_obj=Option.POLARS)
    st.text("2025 Standings:")
    st.dataframe(standings_df, width=400)

with col2:
    results_summary_query = "from reporting.race_results_summary_2025"
    results_summary_df = issue_query(query_str=results_summary_query, return_obj=Option.POLARS)
    st.text("Season results summary:")
    st.dataframe(results_summary_df.sort("avg_result"), width=500)

results_by_race_query = "from reporting.race_results_2025"
results_by_race_df = issue_query(query_str=results_by_race_query, return_obj=Option.POLARS)
st.text("Result by race:")
st.dataframe(results_by_race_df.sort("race_desc", "position"), use_container_width=True)
