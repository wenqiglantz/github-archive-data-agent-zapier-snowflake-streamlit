import streamlit as st
import logging, sys, os
import openai
from dotenv import load_dotenv
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI
from llama_hub.tools.zapier.base import ZapierToolSpec

#loads dotenv lib to retrieve API keys from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# enable INFO level logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# add a title for our UI
st.title("GitHub Archive Analysis")

# add a text area for user to enter SQL query
sql_query = st.text_area("Enter your SQL query here")
if sql_query:

    # establish connection to Snowflake
    conn = st.experimental_connection('snowpark')

    # run query based on the SQL entered 
    df = conn.query(sql_query)

    # write query result on UI
    st.write(df)
    
    # add a line chart to display the result visually
    st.line_chart(df, x="REPO_NAME", y="SUM_STARS")

    # construct zapier_spec by passing in Zapier API key
    zapier_spec = ZapierToolSpec(api_key=os.getenv("ZAPIER_API_KEY"))

    # initialize llm
    llm = OpenAI(model="gpt-3.5-turbo-0613")

    # initialize OpenAI agent by passing in zapier_spec and the llm
    agent = OpenAIAgent.from_tools(zapier_spec.to_tool_list(), verbose=True, llm=llm)

    # add commands
    agent.chat('Send me an email on the details of Significant-Gravitas/Auto-GPT.')
    agent.chat('Add a task to my CoSchedule calendar to check out Significant-Gravitas/Auto-GPT with due date August 3rd 2023.')
