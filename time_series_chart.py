import plotly.graph_objs as go
import streamlit as st
from data_wrangling import get_metric_time_series
from metric_config import metrics, display_metrics

def get_time_series_chart(df, metric):
    """Generates a time series chart for a given metric."""
    data = get_metric_time_series(df, metric)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=data['Day'], y=data['Value'], mode='lines+markers')
        )
    fig.update_layout(
        title=f'{metric.title}',
        xaxis_title='Day',
        yaxis_title=metric.title,
    )
    return fig

def time_series_chart(df):
    """Displays time series charts for selected metrics."""
    with st.container(border=True):        
        chart_tabs = st.tabs(display_metrics)
        for idx, metric in enumerate(display_metrics):
            with chart_tabs[idx]:
                chart = get_time_series_chart(df, metrics[metric])
                st.plotly_chart(chart, use_container_width=True)

