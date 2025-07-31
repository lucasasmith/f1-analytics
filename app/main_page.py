import streamlit as st

st.markdown("# F1 Analytics 🏎️")

description = """This application is built utilizing Python, DuckDB, dbt, Polars, and Streamlit.
More information and the code can be found [here](https://github.com/lucasasmith/f1-analytics). It
is mainly a showcase for Data and Analytics Engineering and simply having fun with data.

Built by [Lucas Smith](www.linkedin.com/in/smithlucas)
"""
st.markdown(description)

st.image("assets/f1_diagram.png")
st.markdown("""

    - Data is first downloaded from GitHub and the [f1db](https://github.com/f1db/f1db) repo.
    - CSV's are extracted.

    dbt:
    - Seeds are utilized to build the bronze layer.
    - Silver/core layer is built to clean and lightly transform the source data. [silver layer tables](https://github.com/lucasasmith/f1-analytics/tree/main/f1_analytics/models/core).
    - Gold/reporting layer is used to provide easy to consume information and statistics. [gold layer views](https://github.com/lucasasmith/f1-analytics/tree/main/f1_analytics/models/reporting).
    - Data tests are incorporate to find issues with the data (verifying primary keys, ranges, etc.).
""")
