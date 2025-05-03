import duckdb
import polars as pl
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# 2025 Teammate Comparison")
st.text("Select a Constructor and see the final position for each driver by race event.")

teams_query = (
    "select distinct constructor_id from core.race_result where year = 2025 order by constructor_id"
)
teams_df = issue_query(query_str=teams_query, return_obj=Option.POLARS)
teams_list = teams_df.get_column("constructor_id").to_list()
constructor_selection = st.selectbox(label="Teams", options=teams_list)

if st.button("Compare"):
    tab1, tab2 = st.tabs(["Qualifying", "Race"])

    with tab1:
        qualy_query = f"""
            select race_desc, driver_id, position
            from reporting.qualifying_results_2025 where constructor_id = '{constructor_selection}'
        """
        qualy_df = issue_query(query_str=qualy_query, return_obj=Option.POLARS)
        st.line_chart(
            data=qualy_df,
            x="race_desc",
            y="position",
            color="driver_id",
            height=500,
            use_container_width=True,
        )
        pivoted_qualy_query = f"""
        with pos as (
            select race_desc, driver_id, position
            from reporting.qualifying_results_2025 where constructor_id = '{constructor_selection}'
        )
        pivot pos
        on driver_id
        using max(position)
        order by race_desc
        """
        pivoted_qualy_df = issue_query(query_str=pivoted_qualy_query, return_obj=Option.POLARS)
        st.dataframe(pivoted_qualy_df)

    with tab2:
        race_query = f"""
            select race_desc, driver_id, position
            from reporting.race_results_2025 where constructor_id = '{constructor_selection}'
        """
        race_df = issue_query(query_str=race_query, return_obj=Option.POLARS)
        st.line_chart(
            data=race_df,
            x="race_desc",
            y="position",
            color="driver_id",
            height=500,
            use_container_width=True,
        )
        pivoted_race_query = f"""
        with pos as (
            select race_desc, driver_id, position
            from reporting.race_results_2025 where constructor_id = '{constructor_selection}'
        )
        pivot pos
        on driver_id
        using max(position)
        order by race_desc
        """
        pivoted_race_df = issue_query(query_str=pivoted_race_query, return_obj=Option.POLARS)
        st.dataframe(pivoted_race_df)
