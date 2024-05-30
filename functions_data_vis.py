import pandas as pd
from langchain.tools import tool

import streamlit as st

##### Data Visualization Functions  

import plotly.graph_objects as go

@tool
def plot_time_series_graph(feature_col: str) -> go.Figure:
  """
  Plots a time series graph from a DataFrame using Plotly and returns the figure object.

  Args:
      feature_col (str): The name of the column containing the feature values to plot.

  Returns:
      go.Figure: The generated Plotly figure object representing the plot.
  """

  try:
    df = st.session_state['data']
    timeseries_col = "Price_Date"
    df[timeseries_col] = pd.to_datetime(df[timeseries_col])  # Convert if necessary

    # Create the time series trace
    trace = go.Scatter(
        x=df[timeseries_col],
        y=df[feature_col],
        mode='lines',
        name=feature_col
    )

    # Create the figure object
    fig = go.Figure(data=[trace])
    fig.update_layout(
        title=f"Time Series of {feature_col}",
        xaxis_title=timeseries_col,
        yaxis_title=feature_col
    )

    return fig

  except Exception as e:
    print(f"Error plotting time series: {e}")
    return None


@tool
def get_null_value_counts(symbol: str) -> pd.DataFrame:
  """
  Returns a DataFrame showing the number of null values in each column.

  Args:
      symbol (str): Dummy Argument

  Returns:
      pd.DataFrame: A new DataFrame with two columns: 'column' (column names) and 'null_count' (number of null values).
  """

  try:
    df = st.session_state['data']
    # Get null value counts
    null_counts = df.isnull().sum()

    # Create DataFrame with column names and null counts
    result_df = pd.DataFrame({'Feature/Column Name': null_counts.index, 'Number of NULL values': null_counts.values})

    return result_df

  except Exception as e:
    print(f"Error getting null value counts: {e}")
    return pd.DataFrame()
