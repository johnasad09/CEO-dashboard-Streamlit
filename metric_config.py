from metric import Metric

def margin_percentage(df):
    """Calculate margin percentage."""
    total_sales = df['Sales'].sum()    
    return df['Gross margin'].sum() / total_sales if total_sales > 0 else 0

def average_transaction_value(df):
    """Calculate average transaction value."""
    total_sales = df['Sales'].sum()
    return total_sales / df['Transactions'].sum() if total_sales > 0 else 0

# Define metrics configuration
metrics = {
    "Total Sales": Metric(
        title="Total Sales",
        func=lambda df: df['Sales'].sum(),
        type="dollars"
    ),
    "Gross margin": Metric(
        title="Gross Margin",
        func=lambda df: df['Gross margin'].sum(),
        type="dollars"
    ),
    "Margin Percentage": Metric(
        title="Margin Percentage",
        func=margin_percentage,
        type="percentage"
    ),
    "Average Transaction Value": Metric(
        title="Average Transaction Value",
        func=average_transaction_value,
        type="dollars"
    )
}

display_metrics = ["Total Sales", "Gross margin", "Margin Percentage", "Average Transaction Value"]

pie_chart_display_metrics = ["Total Sales", "Gross margin"]