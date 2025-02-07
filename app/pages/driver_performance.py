import duckdb
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# Driver Performance (2024)")
st.markdown("### Qualifying performance over the year")
st.markdown("Show the average qualifying position for each driver over the year. Lower is better.")
qualifying_result_query = "from reporting.qualifying_result_over_time"
qualifying_result_df = issue_query(query_str=qualifying_result_query, return_obj=Option.DATAFRAME)
st.line_chart(
    data=qualifying_result_df,
    x="race_desc",
    y="running_avg",
    color="driver_id",
    height=600,
    use_container_width=True,
)

st.markdown("### Race performance over the year")
st.markdown("Show the average finishing position for each driver over the year. Lower is better.")
race_result_query = "from reporting.race_result_over_time"
race_result_df = issue_query(query_str=race_result_query, return_obj=Option.DATAFRAME)
st.line_chart(
    data=race_result_df,
    x="race_desc",
    y="running_avg",
    color="driver_id",
    height=600,
    use_container_width=True,
)
