import streamlit as st
import pandas as pd
from pathlib import Path

"""Path(__file__) creates an object of path
    resolve() returns the absolute path
    parent gives the directory containing the file
"""
BASE_DIR = Path(__file__).resolve().parent
SALES_DATA_PATH = BASE_DIR / "sales_data.csv"


def load_data():
    """Load data from a CSV file."""
    return pd.read_csv(SALES_DATA_PATH)

