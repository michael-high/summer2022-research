import requests
from datetime import date
today = date.today()

prompt=""
with open("C:\CS\SUM2022\Jurassic\prompt.txt", "r") as k:
    for j in k:
        prompt+=(j)
#print(prompt)
x=requests.post("https://api.ai21.com/studio/v1/j1-jumbo/complete",
    headers={"Authorization": "Bearer oEK0eJXzKWfeEH55MjUg2FKJiJsCz9R9"},
    json={
        "prompt": prompt,
        "numResults": 1,
        "maxTokens": 64,
        "temperature": 0.0,
        "topKReturn": 0,
        "topP":1,
        "countPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "frequencyPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "presencePenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
      },
      "stopSequences":["###"]
    }
)
with open("Jumbo1-tests.txt", "a")as h:
    h.write("\n-------------3.1-Comp-Simpl-Jumbo1---------"+str(today)+"--------\n"+prompt+"\n")
    h.write(x.json()["completions"][0]["data"]["text"])
    
    
    
    
    
    
    
    






# print(x)
# print(type(x))
# print(x.text)
# print(type(x.text))
# print(x.content)
# print(type(x.content))
# print(x.url)
# print(type(x.url))
# print(x.headers)
# print(type(x.headers))
#print(x._content))