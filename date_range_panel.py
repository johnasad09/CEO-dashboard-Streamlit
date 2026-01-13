import streamlit as st
import pandas as pd
from datetime import date, timedelta

# Define constants for default date range
# Assuming the latest date in the dataset is 2024-08-31
# if the dataset is dynamic, then we would replace this with LATEST_DATE = date.today()
LATEST_DATE = date.fromisoformat("2024-08-31")
# Set default start date to 30 days before the latest date
THIRTY_DAYS_AGO = LATEST_DATE - timedelta(days=30)

def get_compare_range(start, end, comparison):
    offsets = {
        "MoM": pd.DateOffset(months=1),
        "QoQ": pd.DateOffset(months=3),
        "YoY": pd.DateOffset(years=1),
        "Previous Period": pd.DateOffset(days=(end - start).days + 1)
    }
    offset = offsets[comparison]
    return (start - offset).date(), (end - offset).date()

def date_range_panel():
    """Creates a date range panel in Streamlit and returns selected start and end dates."""
    if 'w:start' not in st.session_state:
        st.session_state['w:start'] = THIRTY_DAYS_AGO
    if 'w:end' not in st.session_state:
        st.session_state['w:end'] = LATEST_DATE
    start = st.date_input("Start date", key="w:start")
    end = st.date_input("End date", key="w:end")
    comparison = st.selectbox(
        "Compare to", ["MoM", "QoQ", "YoY", "Previous Period"], key="w:compare")
    compare_start, compare_end = get_compare_range(start, end, comparison)
    st.info(f"Comparing with: \n{compare_start} to {compare_end}")
    return start, end, compare_start, compare_end