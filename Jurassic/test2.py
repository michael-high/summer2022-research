import requests

requests.post(
    "https://api.ai21.com/studio/v1/j1-large/complete",
    headers={"Authorization": "Bearer oEK0eJXzKWfeEH55MjUg2FKJiJsCz9R9"},
    json={
        "prompt": "Life is like", 
        "numResults": 1, 
        "maxTokens": 8, 
        "stopSequences": ["."],
        "topKReturn": 0,
        "temperature": 0.0
    }
)
