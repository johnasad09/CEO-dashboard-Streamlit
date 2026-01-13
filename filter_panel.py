import streamlit as st
from data_wrangling import get_unique_values, apply_filters

# Define the dimensions to filter on
filter_dims = ["Age group", "Gender", "Category", "Segment", "Product name", "State"]

def filter_panel(df):
    """Creates a filter panel in Streamlit and returns selected filters."""
    # Dictionary to hold selected filters
    filters = {}
    # Create an expander for filters
    with st.expander('Filters'):
        # Create columns for each filter dimension
        filter_cols = st.columns(len(filter_dims))
        effective_df = df
        # Iterate through each filter dimension and create multiselect widgets
        for idx, dim in enumerate(filter_dims):
            # Create multiselect in the respective column
            with filter_cols[idx]:
                effective_df = apply_filters(effective_df, filters)
                # Get unique values for the dimension
                unique_values = get_unique_values(effective_df, dim)
                # Create multiselect widget
                filters[dim] = st.multiselect(dim, unique_values, key=f'w:filter|{dim}')
    return filters
