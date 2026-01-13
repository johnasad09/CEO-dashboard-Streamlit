import streamlit as st
# from data_loader import load_data
from filter_panel import filter_panel
from data_wrangling import prep_data, get_filtered_data_within_date_range
from date_range_panel import date_range_panel
from metric_bar import metric_bar
from time_series_chart import time_series_chart
from pie_chart import pie_chart
from drilldown import drilldown
from query_params import set_widget_defaults, set_params

# set page layout to wide
st.set_page_config(layout="wide")
set_widget_defaults()
with st.sidebar:
    dd_button_container = st.container()
    start, end, compare_start, compare_end = date_range_panel()

# Load and prepare data
data = prep_data()
# Create filter panel and get selected filters
filters = filter_panel(data)
# Apply filters to the data
main_df = get_filtered_data_within_date_range(data, start, end, filters)
if main_df.empty:
    st.warning("No data to display for the selected filters and date range.")
else:
    compare_df = get_filtered_data_within_date_range(data, compare_start, compare_end, filters)
    if dd_button_container.button("Drilldown", width='stretch'):
        drilldown(main_df, compare_df)
    time_series_col, pie_chart_col = st.columns(2)
    with time_series_col:
        time_series_chart(main_df)
    with pie_chart_col:
        pie_chart(main_df)
# st.write(main_df.head(5))
set_params()