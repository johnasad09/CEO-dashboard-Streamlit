import plotly.graph_objs as go
import streamlit as st
from data_wrangling import get_metric_grouped_by_dimensions
from metric_config import metrics, pie_chart_display_metrics

def get_pie_chart(df, metric, dimension):
    """Generates a pie chart for a given metric grouped by a specified dimension."""
    data = get_metric_grouped_by_dimensions(df, metric, dimension)
    fig = go.Figure()
    fig.add_trace(
        go.Pie(labels=data[dimension], values=data['Value'], hole=0.4)
    )
    return fig

def pie_chart(df):
    """Displays pie charts for selected metrics grouped by a specified dimension."""
    with st.container(border=True):
        split_dimension = st.selectbox(
            "Group By",
            options=["Age group", "Gender", "State", "Category", "Segment", "Product name"],
            # options=["Age group", "Gender", "Category", "Segment", "Product name", "State"],
        
        )
        metric_tabs = st.tabs(pie_chart_display_metrics)
        for idx, metric in enumerate(pie_chart_display_metrics):
            with metric_tabs[idx]:
                chart = get_pie_chart(df, metrics[metric], dimension=split_dimension)
                st.plotly_chart(chart, use_container_width=True)