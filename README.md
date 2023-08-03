# github-archive-data-agent-zapier-snowflake-streamlit
GitHub Archive Data Analysis with LlamaIndex Data Agents, Zapier NLA, Snowflake, and Streamlit. Check out my blog [Low-Code and No-Code Task Automation With LlamaIndex Data Agents, Zapier NLA, Snowflake, and Streamlit](https://betterprogramming.pub/low-code-and-no-code-task-automation-with-llamaindex-data-agents-zapier-nla-snowflake-85f2ab6144fe?sk=f7f94ba7844c8268b6e708f6d4c7b6c1) for details.

## Application Setup

```
conda create --name py38_env
conda activate py38_env
pip install -r requirements.txt
```

Add `.env` file at the project root and replace placeholders with your API keys:
```
OPENAI_API_KEY=<YOUR-API-KEY>
ZAPIER_API_KEY=<YOUR-API-KEY>
```

Add `secrets.toml` to `.streamlit` directory at project root, replace placeholders with your Snowflake connection details:
```
# .streamlit/secrets.toml

[connections.snowpark]
account = "<ORG>-<ACCOUNT>"
user = "<USERNAME>"
password = "<PASSWORD>"
role = "ACCOUNTADMIN"
warehouse = "<WAREHOUSE-NAME>"
database = "CYBERSYN_GITHUB_ARCHIVE"
schema = "CYBERSYN"
client_session_keep_alive = true
```

Run the app by kicking off this command:
```
streamlit run github-archive.py
```

