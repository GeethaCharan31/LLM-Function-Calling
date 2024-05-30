import pandas as pd
from langchain.tools import tool

import streamlit as st

##### Time Series Imputation Functions

@tool
def impute_missing_value_using_spline_imputation(column_name: str) -> pd.DataFrame:
    """
    Imputes missing values in a column using quadratic spline interpolation.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        st.write("From Spline")
        st.write(st.session_state['data'])
        data_imputed = st.session_state['data']

        # Get indices of missing values (can be improved for efficiency with notna())
        data_series = data_imputed[column_name]
        missing_indexes = data_series.isnull().index  # Indexes of missing values

        # Interpolate missing values using spline interpolation with order 2 and fill gaps in both directions
        data_series_imputed = data_series.interpolate(method='spline', order=2, limit_direction='both')

        # Replace the original column with the imputed values based on indexes
        data_imputed.loc[missing_indexes, column_name] = data_series_imputed
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()


@tool
def impute_missing_value_using_linear_imputation(symbol: str) -> pd.DataFrame:
    """
    Imputes missing values in a column using linear interpolation.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        # Copy the data to avoid modifying the original
        data_imputed = st.session_state['data']

        # Get indices of missing values (can be improved for efficiency with notna())
        data_series = data_imputed[column_name]
        missing_indexes = data_series.isnull().index  # Indexes of missing values

        # Interpolate missing values using linear interpolation
        data_series_imputed = data_series.interpolate(method='linear')

        # Replace the original column with the imputed values based on indexes
        data_imputed.loc[missing_indexes, column_name] = data_series_imputed
        st.session_state['data'] = data_imputed
        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()
    
@tool
def impute_missing_value_using_back_fill_imputation(symbol: str) -> pd.DataFrame:
    """
    Imputes missing values in a column using backfill interpolation.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        # Copy the data to avoid modifying the original
        data_imputed = st.session_state['data']

        # Get indices of missing values (can be improved for efficiency with notna())
        data_series = data_imputed[column_name]
        missing_indexes = data_series.isnull().index  # Indexes of missing values

        # Interpolate missing values using backfill interpolation
        data_series_imputed = data_series.interpolate(method='bfill')

        # Replace the original column with the imputed values based on indexes
        data_imputed.loc[missing_indexes, column_name] = data_series_imputed
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()

@tool
def impute_missing_value_using_forward_fill_imputation(symbol: str) -> pd.DataFrame:
    """
    Imputes missing values in a column using forward interpolation.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        # Copy the data to avoid modifying the original
        data_imputed = st.session_state['data']

        # Get indices of missing values (can be improved for efficiency with notna())
        data_series = data_imputed[column_name]
        missing_indexes = data_series.isnull().index  # Indexes of missing values

        # Interpolate missing values using forward interpolation
        data_series_imputed = data_series.interpolate(method='ffill')

        # Replace the original column with the imputed values based on indexes
        data_imputed.loc[missing_indexes, column_name] = data_series_imputed
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()


# function merging linear,backfill,forward
@tool
def impute_missing_values_using_method_specified_by_user(imputation_method: str, symbol: str) -> pd.DataFrame:
    """
    Imputes missing values in a column using backfill interpolation.

    Args:
    imputation_method (str): Imputation Method which is passed as argument for data_series.interpolate
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        # Copy the data to avoid modifying the original
        data_imputed = st.session_state['data']

        # Get indices of missing values (can be improved for efficiency with notna())
        data_series = data_imputed[column_name]
        missing_indexes = data_series.isnull().index  # Indexes of missing values

        # Interpolate missing values using backfill interpolation
        #   imputation_method = imputation_method.lower()
        if imputation_method == "forward" or imputation_method == "forward fill" or imputation_method == "forward_fill":
            imputation_method = "ffill"
        if imputation_method == "backward" or imputation_method == "backward fill" or imputation_method == "backward_fill":
            imputation_method = "bfill"
        
        data_series_imputed = data_series.interpolate(method=imputation_method)

        # Replace the original column with the imputed values based on indexes
        data_imputed.loc[missing_indexes, column_name] = data_series_imputed
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()
    








# Tabular Imputation Techniques
@tool
def impute_missing_value_using_mean(symbol: str) -> pd.DataFrame:
    """
    Impute Missing Values of a column in a dataset using Mean.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        data_imputed = st.session_state['data']
        # Fill missing values with the mean of the column
        data_imputed[column_name] = data_imputed[column_name].fillna(data_imputed[column_name].mean())
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()

@tool
def impute_missing_value_using_mode(symbol: str) -> pd.DataFrame:
    """
    Impute Missing Values of a column in a dataset using mode.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        data_imputed = st.session_state['data']

        # Get the mode of the column (most frequent value)
        mode_value = data_imputed[column_name].mode().iloc[0]  # Access the first element

        # Replace missing values with the mode
        data_imputed.loc[data_imputed[column_name].isnull(), column_name] = mode_value
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()
    
# @tool
# def impute_missing_value_using_standard_deviation(symbol: str) -> pd.DataFrame:
#     """
#     Impute Missing Values of a column in a dataset using standard_deviation.

#     Args:
#     symbol (str): Column/Feature name that is to be imputed.

#     Returns:
#     pd.DataFrame: Imputed Dataframe.
#     """
#     try:
#         column_name = symbol
#         df[column_name] = df[column_name].fillna(df[column_name].std())
#         return df
    
#     except Exception as e:
#         print(f"Error Imputing the DataFrame: {e}")
#         return pd.DataFrame()
    
@tool
def impute_missing_value_using_min_value(symbol: str) -> pd.DataFrame:
    """
    Impute Missing Values of a column in a dataset using min_value.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        data_imputed = st.session_state['data']

        # Fill missing values with the minimum value in the column
        data_imputed[column_name] = data_imputed[column_name].fillna(data_imputed[column_name].min())
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()
    

@tool
def impute_missing_value_using_max_value(symbol: str) -> pd.DataFrame:
    """
    Impute Missing Values of a column in a dataset using max_value.

    Args:
    symbol (str): Column/Feature name that is to be imputed.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        column_name = symbol
        data_imputed = st.session_state['data']

        # Fill missing values with the minimum value in the column
        data_imputed[column_name] = data_imputed[column_name].fillna(data_imputed[column_name].max())
        st.session_state['data'] = data_imputed

        return data_imputed
    
    except Exception as e:
        print(f"Error Imputing the DataFrame: {e}")
        return pd.DataFrame()