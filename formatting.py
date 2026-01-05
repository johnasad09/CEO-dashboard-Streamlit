import humanize

def format_metric(value, metric_type):
    """Format the metric value based on its type."""
    if metric_type == "dollars":
        return f"${humanize.metric(value)}"
    elif metric_type == "percentage":
        return f"{round(value * 100, 1)}%"
    else:
        return f'{(value)}'