import streamlit as st
from datetime import date, timedelta

# Define constants for default date range
# Assuming the latest date in the dataset is 2024-08-31
# if the dataset is dynamic, then we would replace this with LATEST_DATE = date.today()
LATEST_DATE = date.fromisoformat("2024-08-31")
# Set default start date to 30 days before the latest date
THIRTY_DAYS_AGO = LATEST_DATE - timedelta(days=30)

def date_range_panel():
    """Creates a date range panel in Streamlit and returns selected start and end dates."""
    start = st.date_input("Start date", value=THIRTY_DAYS_AGO,)
    end = st.date_input("End date", value=LATEST_DATE)
    return start, end