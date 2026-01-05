import streamlit as st
import pandas as pd
from data_loader import load_data

# Cache cleaned data for 12 hours (ttl="12h")
@st.cache_data(show_spinner="Reading sales data", ttl="12h")  
def prep_data() -> pd.DataFrame:
    """Prepares and cleans the sales data for analysis."""
    df = clean_column_names(load_data())
    # Convert 'Date' column to datetime and create 'Day' column
    df['Day'] = pd.to_datetime(df['Date'])
    return df

# New function to get unique values from a DataFrame column
def get_unique_values(df, column_name):
    """Returns unique values from a specified column in the DataFrame."""
    return list(df[column_name].unique())

# New function to clean column names
def clean_column_names(df):
    """Cleans column names by stripping whitespace and converting to lowercase."""
    df.columns = df.columns.str.replace('_', ' ').str.strip().str.capitalize()
    return df

# New function to apply filters
def apply_filters(df, filters):
    """Applies the selected filters to the DataFrame."""
    # Iterate through each filter and apply it to the DataFrame
    for column, selected_values in filters.items():
        # Check if there are selected values for the column
        if selected_values:
            # Filter the DataFrame based on selected values
            df = df[df[column].isin(selected_values)]
    return df

# New function to filter data by date range
def get_data_within_date_range(df, start_date, end_date):
    """Filters the DataFrame to include only rows within the specified date range."""
    
    if start_date is not None and end_date is not None:
        # Convert start and end dates to datetime objects for comparison
        date_start, date_end = pd.to_datetime(start_date), pd.to_datetime(end_date)
        # Filter the DataFrame based on the date range
        return df[(df['Day'] >= date_start) & (df['Day'] <= date_end)]
    
    return df

def get_filtered_data_within_date_range(df, start_date, end_date, filters):
    """Applies filters and date range to the DataFrame."""
    # 
    df_within_range = get_data_within_date_range(df.copy(), start_date, end_date)
    return apply_filters(df_within_range, filters)

def get_metric_time_series(df, metric):
    """Generates time series data for a given metric."""
    grouped = df.groupby('Day')
    data = grouped.apply(
        metric.func, include_groups=False
    ).reset_index()
    data.columns = ['Day', 'Value']
    return data

def get_metric_grouped_by_dimensions(df, metric, dimension):
    """Generates metric data grouped by a specified dimension."""
    grouped = df.groupby(dimension)
    data = grouped.apply(
        metric.func, include_groups=False
    ).reset_index()
    data.columns = [dimension, "Value"]
    return data


