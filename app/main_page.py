import streamlit as st

st.markdown("# F1 Analytics 🏎️")

description = """This application is built utilizing Python, DuckDB, dbt, Polars, and Streamlit.
More information and the code can be found [here](https://github.com/lucasasmith/f1-analytics). It
is mainly a showcase for Data Engineering and having fun with data. Enjoy :smiley:.

Built by [Lucas Smith](www.linkedin.com/in/smithlucas)
"""
st.markdown(description)

st.image("assets/f1_diagram.png")
st.markdown("""

    Data is first downloaded from GitHub and the [f1db](https://github.com/f1db/f1db) repo. CSV's
    are extracted from the newest release and inserted into the existing dbt structure.

    DuckDB is utilized to store the data.

    dbt is used to:
    - load the inital raw CSV's into the `raw` schema.
    - create `core` [silver layer tables](https://github.com/lucasasmith/f1-analytics/tree/main/f1_analytics/models/core).
    - create `reporing` [gold layer views](https://github.com/lucasasmith/f1-analytics/tree/main/f1_analytics/models/reporting).
    - run data tests (verifying primary keys, ranges, etc.)
""")
