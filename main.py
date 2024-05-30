import streamlit as st
import pandas as pd

# import argparse
# from io import StringIO

from functioncall import ModelInference

# parser = argparse.ArgumentParser(description="Run recursive function calling loop")
# parser.add_argument("--model_path", type=str, help="Path to the model folder")
# parser.add_argument("--chat_template", type=str, default="chatml", help="Chat template for prompt formatting")
# parser.add_argument("--num_fewshot", type=int, default=None, help="Option to use json mode examples")
# parser.add_argument("--load_in_4bit", type=str, default="False", help="Option to load in 4bit with bitsandbytes")
# parser.add_argument("--query", type=str, default="I need the current stock price of Tesla (TSLA)")
# parser.add_argument("--max_depth", type=int, default=5, help="Maximum number of recursive iteration")
# args = parser.parse_args()

st.set_page_config(
        page_title="Agri-Vaahan LLM",
        page_icon="✨",
    )

st.title('AGRI-VAAHAN PLUS ✨')


########################## 1. DATA UPLOAD

# Check if 'data' key exists in session_state, otherwise set it to None
if 'data' not in st.session_state:
  st.session_state['data'] = None

uploaded_file = st.file_uploader("Upload CSV or XLSX file", type=['csv', 'xlsx'])
header_row = st.number_input('Select header row',min_value=0,value=0)

if uploaded_file is not None:
  # Read the uploaded file based on its type
  if uploaded_file.type == 'text/csv':
    df = pd.read_csv(uploaded_file, header=header_row)
  elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
    df = pd.read_excel(uploaded_file, header=header_row)
  else:
    st.error("Please upload a CSV or XLSX file only.")

  # Add the DataFrame to session_state
  if st.session_state['data'] is None:
    st.session_state['data'] = df.copy()

  st.success("File uploaded successfully!")

# Check if data exists in session_state, then use it
if st.session_state['data'] is not None:
  # You can now access the DataFrame using st.session_state['data']
  # Perform any operations on the data here
  st.write(st.session_state['data'])  # Display the first few rows



########################## 2. HERMES MODEL 

# Initializing Chat
prompt = st.chat_input("Say something")

# arguments
chat_template = "chatml"
num_fewshot = None
load_in_4bit = "False"
max_depth = 5


if "llm" not in st.session_state:
   model_path = 'NousResearch/Hermes-2-Pro-Llama-3-8B'
   st.session_state["llm"] = ModelInference(model_path, chat_template, load_in_4bit)


if prompt:
    st.chat_message("user").write(prompt)
    # model_path = 'NousResearch/Hermes-2-Pro-Llama-3-8B'
    # inference = ModelInference(model_path, chat_template, load_in_4bit)
    # Run the model evaluator
    inference = st.session_state["llm"]
    assistant_response = inference.generate_function_call(prompt, chat_template, num_fewshot, max_depth)
    
    import time
    def stream_data():
        for word in assistant_response.split(" "):
            yield word + " "
            time.sleep(0.07)
    st.chat_message("assistant").write_stream(stream_data)

# streamlit run main.py --server.fileWatcherType none