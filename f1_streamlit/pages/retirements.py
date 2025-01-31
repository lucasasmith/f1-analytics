import duckdb
import streamlit as st

st.set_page_config(layout="wide")
st.markdown("# F1 Retirement Analysis")


def issue_query(query_str: str):
    with duckdb.connect("../f1_analytics/f1.db") as conn:
        return conn.sql(query_str).df()


st.markdown("### Retirements by year")
yearly_retirements_query = """
    select
        race.year,
        count(0) as retirement_count
    from core.race_result as rr
    inner join core.race
    using(race_id)
    where
        rr.reason_retired is not null
    group by
        all
"""
yearly_retirements_df = issue_query(yearly_retirements_query)
st.bar_chart(
    data=yearly_retirements_df,
    x="year",
    y="retirement_count",
    color="#88ffe6",
    use_container_width=True,
)
st.markdown("""Here we have a breakdown of the number of retirements by year and wow, 1984 was a 
            rough year for the cars and teams.""")
with st.expander("See query"):
    st.code(yearly_retirements_query)

st.markdown("""This only tells some of the story though. Since the number of races per year can 
            vary, lets calculate the ratio of average retirements per race by year.""")
yearly_average_retirements_per_race_query = """
    select
        race.year,
        round(count(rr.reason_retired) /
        count(distinct race.race_id), 1) as ratio
    from
        core.race_result as rr
        inner join core.race
        using(race_id)
    group by
        all
"""
yearly_average_retirements_per_race_df = issue_query(yearly_average_retirements_per_race_query)
st.bar_chart(
    data=yearly_average_retirements_per_race_df,
    x="year",
    y="ratio",
    color="#ff88dd",
    use_container_width=True,
)
with st.expander("See query"):
    st.code(yearly_average_retirements_per_race_query)
st.markdown("""You can see the data doesn't change the picture by much. But, the year **2020** for 
            example, shows us a higher retirement ratio by race. This also shows us **2024** was 
            indeed the most reliable F1 season in history and the early **2000's** marked a quite
            dramatic shift in reliability.""")

st.markdown("Lastly, summarize all the reasons for retirement by count.")
reason_retired_count_query = """
    select
        lower(reason_retired) reason_retired,
        count(0) as count
    from
        core.race_result
    where
        reason_retired is not null
    group by
        all
    having
        count >= 5
"""
reason_retired_count_df = issue_query(reason_retired_count_query)
st.bar_chart(
    data=reason_retired_count_df,
    x="reason_retired",
    y="count",
    color="#a2ff88",
    horizontal=True,
    use_container_width=True,
)
with st.expander("See query"):
    st.code(reason_retired_count_query)
st.markdown("""
    We can see that the most common reason for an F1 retirement is an engine issue.
    This large variety of retirement reasons could use some more generalizing. I
    added a filter where a retirement reason needs to have occurred at least 5 times to be 
    included.
""")
