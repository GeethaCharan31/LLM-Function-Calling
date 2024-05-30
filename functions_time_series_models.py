import pandas as pd
from langchain.tools import tool

import streamlit as st

##### Time Series Forecasting

@tool
def auto_arima(column_name: str): #-> pd.DataFrame:
    """
    Forecast using ARIMA.

    Args: symbol (str): Column/Feature name.

    Returns:
    pd.DataFrame: Imputed Dataframe.
    """
    try:
        # st.write("From Spline")
        # st.write(st.session_state['data'])
        df = st.session_state['data']
        from darts.models import AutoARIMA
        from darts.timeseries import TimeSeries
        model = AutoARIMA(start_p=5, max_p=12, start_q=1)
        print(model)
        series = TimeSeries.from_dataframe(df, time_col="Price_Date", value_cols=[column_name])
        model.fit(series)
        pred = model.predict(6)
        st.write(pred.values())
        # st.session_state['data'] = df_pred

        return pred.values()
    
    except Exception as e:
        print(f"Error Predicing: {e}")
        return pd.DataFrame()
