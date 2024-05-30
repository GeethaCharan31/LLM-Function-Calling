from typing import List
from langchain.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool



# import agri-vaahan customs functions here

from functions_data_imputing import (
    impute_missing_value_using_spline_imputation,
    impute_missing_value_using_linear_imputation,
    impute_missing_value_using_back_fill_imputation,
    impute_missing_value_using_forward_fill_imputation,
    impute_missing_values_using_method_specified_by_user,
    #
    impute_missing_value_using_mean,
    impute_missing_value_using_mode,
    impute_missing_value_using_min_value,
    impute_missing_value_using_max_value,
)

from functions_data_cleaning import (
    drop_feature_column,
    remove_row_by_index,
    extract_data_between_dates,
    remove_duplicate_rows,
)

from functions_data_vis import(
    plot_time_series_graph,
    get_null_value_counts,
)

from functions_time_series_models import(
    auto_arima,
)

def get_openai_tools() -> List[dict]:
    functions = [    
        impute_missing_value_using_mean,
        impute_missing_value_using_spline_imputation,
        impute_missing_value_using_linear_imputation,
        impute_missing_value_using_back_fill_imputation,
        impute_missing_value_using_forward_fill_imputation,
        #impute_missing_values_using_method_specified_by_user, # currently raises error str- handlers as any function with two arguments is not getting called
        impute_missing_value_using_mode,
        impute_missing_value_using_min_value,
        impute_missing_value_using_max_value,

        # data cleaning functions
        drop_feature_column,
        remove_row_by_index,
        extract_data_between_dates, # currently raises error str- handlers as any function with two arguments is not getting called
        remove_duplicate_rows,

        # data vis functions
        plot_time_series_graph,
        get_null_value_counts,

        # models
        auto_arima,
    ]

    # BELOW COMMENTED CODE IS TO VIEW THE JSON-TOOLS
    # import json  # Assuming convert_to_openai_tool returns JSON-serializable data

    # def write_tools_to_file(tools, filename):
    #     """Writes a list of tools to a file in JSON format.

    #     Args:
    #         tools: A list of tools (presumably dictionaries or other JSON-serializable data).
    #         filename: The name of the file to write to.
    #     """
    #     with open(filename, 'w') as f:
    #         json.dump(tools, f, indent=2)  # Add indent for readability

    # # Assuming functions is already defined and contains functions to convert
    # tools = [convert_to_openai_tool(f) for f in functions]
    # write_tools_to_file(tools, "converted_tools_2.json")  # Replace with your desired filename


    tools = [convert_to_openai_tool(f) for f in functions]

    return tools