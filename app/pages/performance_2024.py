import duckdb
import streamlit as st

st.set_page_config(layout="wide")
st.markdown("# F1 Qualifying Performance")


def issue_query(query_str: str):
    with duckdb.connect("../f1_analytics/f1.db") as conn:
        return conn.sql(query_str).df()


st.markdown("### Qualifying performance over the year")
qualifying_result_query = "select * from reporting.qualifying_result_over_time"
qualifying_result_df = issue_query(qualifying_result_query)
st.line_chart(
    data=qualifying_result_df,
    x="race_desc",
    y="running_avg",
    color="driver_id",
    height=600,
    use_container_width=True,
)
st.markdown("""This graph attemps to show the running average qualifying position for a driver
    throughout the year. It helps to see if a team is improving over the year (see Mclaren drvers)
    or if performance is decreasing over a year (see Red Bull drivers).""")

st.markdown("### Race performance over the year")
race_result_query = "select * from reporting.race_result_over_time"
race_result_df = issue_query(race_result_query)
st.line_chart(
    data=race_result_df,
    x="race_desc",
    y="running_avg",
    color="driver_id",
    height=600,
    use_container_width=True,
)
