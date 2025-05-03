import altair as alt
import streamlit as st

from pages import Option, issue_query

st.set_page_config(layout="wide")
st.markdown("# 2025 Teammate Comparison")
st.text("Select a Constructor and see the final position for each driver by race event.")


def build_chart(df):
    # Create a selection that chooses the nearest point & selects based on x-value
    nearest = alt.selection_point(nearest=True, on="pointerover", fields=["race_desc"], empty=False)
    # The basic line
    line = (
        alt.Chart(df)
        .mark_line(interpolate="natural")
        .encode(x="race_desc", y="position", color=alt.Color("driver_id").legend(None))
        .properties(width=1000)
    )
    when_near = alt.when(nearest)
    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(opacity=when_near.then(alt.value(1)).otherwise(alt.value(0)))
    # Draw a rule at the location of the selection
    rules = (
        alt.Chart(df)
        .transform_pivot("driver_id", value="position", groupby=["race_desc"])
        .mark_rule(color="orange", strokeWidth=2)
        .encode(
            x="race_desc",
            opacity=when_near.then(alt.value(0.3)).otherwise(alt.value(0)),
            tooltip=[alt.Tooltip(c, type="quantitative") for c in df["driver_id"]],
        )
        .add_params(nearest)
    )

    label = line.encode(
        x=alt.X("race_desc", title="").aggregate(argmax="race_desc"),
        y=alt.Y("position", title="").aggregate(argmax="race_desc"),
        text="driver_id",
    )
    # Create a text label
    text = label.mark_text(align="left", dx=7)
    # Put the five layers into a chart and bind the data
    return line + points + rules + text


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
        st.altair_chart(
            build_chart(qualy_df),
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
        st.altair_chart(
            build_chart(race_df),
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
