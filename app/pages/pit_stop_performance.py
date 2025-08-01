"""Page to visualize pit stop performance."""

import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# Team Pit Stop Performance (2014-Present)")
st.markdown(
    """Show the average team pit stop ranking by season. The average is calculated by rank for each
    race over the season. Lower is better."""
)

pit_stop_perf_query = "from reporting.pit_stop_over_time"
pit_stop_perf_df = issue_query(query_str=pit_stop_perf_query, return_obj=Option.POLARS)
st.line_chart(
    data=pit_stop_perf_df,
    x="year",
    y="season_rank_avg",
    color="constructor_id",
    height=600,
    use_container_width=True,
)
if st.button(label="Show table"):
    st.dataframe(data=pit_stop_perf_df.sort("year", "season_rank_avg", descending=[True, False]))
