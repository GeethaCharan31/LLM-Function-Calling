import pandas as pd
from langchain.tools import tool
import streamlit as st

##### Data Cleaning Functions

@tool
def drop_feature_column(symbol: str) -> pd.DataFrame:
    """
    Drop Feature Column from the DataFrame

    Args:
    symbol (str): Column/Feature name that is to be dropped.

    Returns:
    pd.DataFrame: Updated Dataframe.
    """
    try:
        df = st.session_state['data']
        column_name = symbol
        # Copy the data to avoid modifying the original
        df.drop(column_name, axis=1, inplace=True)
        st.session_state['data'] = df
        return df
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()  

@tool
def remove_row_by_index(symbol: str) -> pd.DataFrame:
    """
    Drop Rows based on index from the DataFrame

    Args:
    symbol (str): Row ID name that is to be dropped.

    Returns:
    pd.DataFrame: Updated Dataframe.
    """
    try:
        df = st.session_state['data']
        row_id = int(symbol)
        # Copy the data to avoid modifying the original
        df.drop(row_id, axis=0, inplace=True)
        st.session_state['data'] = df
        return df
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame() 

@tool
def remove_duplicate_rows(symbol: str) -> pd.DataFrame:
  """
  Removes duplicate rows from a DataFrame based on specified columns.
  Args: None
  Returns: pd.DataFrame: A new DataFrame with duplicate rows removed.
  """

  try:
    # Remove duplicates based on specified columns (or all columns if subset is None)
    df = st.session_state['data']
    df_dropped = df.drop_duplicates(subset=None)
    st.session_state['data'] = df_dropped
    return df_dropped

  except Exception as e:
    print(f"Error removing duplicates: {e}")
    return pd.DataFrame()



# @tool
# def extract_data_between_dates(date1: str, date2:str) -> pd.DataFrame:
#     """
#     Extract Rows between two dates from the DataFrame

#     Args:
#     date1 (str): Initial Date.
#     date2 (str): Final Date

#     Returns:
#     pd.DataFrame: Updated Dataframe.
#     """
#     try:
#         from dateutil.parser import parse

#         # Convert string to datetime object (may attempt format detection)  , final_date:str
#         print(f"initial_date {date1}")
#         initial_date = parse(date1)
#         # final_date = "1st Jan 2018"
#         final_date = parse(date2)

#         date_column = "Price_Date"
#         df[date_column] = pd.to_datetime(df[date_column])  
#         filtered_df = df[(df[date_column] >= initial_date) & (df[date_column] <= final_date)]

#         return filtered_df
    
#     except Exception as e:
#         print(f"Error Imputing the DataFrame: {e}")
#         return pd.DataFrame()   

from typing import Dict
@tool
def extract_data_between_dates(tool_input: Dict[str,str]) -> pd.DataFrame:
    """
    Extract Rows between two dates from the DataFrame
    Args:
        tool_input (Dict): Dictionary containing the following keys:
            'date1' (str): Initial Date.
            'date2' (str): Final Date.
    Returns:
        pd.DataFrame: Updated Dataframe.
    """
    try:
        df = st.session_state['data']
        from dateutil.parser import parse
        date1 = tool_input.get('date1', None)
        date2 = tool_input.get('date2', None)
        
        if date1 is None or date2 is None:
            raise ValueError("Both 'date1' and 'date2' must be provided.")
        
        # Convert string to datetime object (may attempt format detection)
        initial_date = parse(date1)
        final_date = parse(date2)
        date_column = "Price_Date"
        df[date_column] = pd.to_datetime(df[date_column])
        filtered_df = df[(df[date_column] >= initial_date) & (df[date_column] <= final_date)]
        st.session_state['data'] = filtered_df
        return filtered_df
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()   