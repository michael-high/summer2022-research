import requests
from datetime import date
import random

today = date.today()

prompt_pool="\n"
with open("C:\CS\SUM2022\Jurassic\prompt.txt", "r") as k:
    for j in k:
        prompt_pool+=(j)
#print(prompt_pool)
prompt_array=prompt_pool.split("###")
#print(prompt_array)
header="""
___________________________________________________________________________________________________

                -----------------   EXPERIMENT #     -------------------
___________________________________________________________________________________________________
    """
with open("jul-11-Jumbo1.txt", "a")as h:
    h.write(header)
    correct=0
    for i in range(0,len(prompt_array)):
        prompt=""
        prompt_shuffle=[]
        for j in range(0,len(prompt_array)):
            if i!=j:
                prompt_shuffle.append(prompt_array[j])
        #print(prompt_shuffle)
        random.shuffle(prompt_shuffle)
        #print(prompt_shuffle)
        for k in range(0,len(prompt_shuffle)):
            prompt+=prompt_shuffle[k]+"###"
        target=prompt_array[i].split("Proof:")
        question=target[0]
        expected="Proof:"+target[1]
        prompt+=question
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
        #with open("autotest-trials.txt", "a")as h:
        h.write("\n-------------"+str(i)+"-tollens-Jumbo1---------"+str(today)+"--------\n"+prompt+"\n")
        h.write(x.json()["completions"][0]["data"]["text"])

        out=str(x.json()["completions"][0]["data"]["text"])
        lst_out=[out]
        print(str(lst_out))
        out_2=[expected]
        print(str(out_2))


        if str(x.json()["completions"][0]["data"]["text"])==str(expected):
            correct+=1
            h.write(str(expected)+"\n         ------WORD FOR WORD------             "+str(correct)+"/"+str(len(prompt_array))+"\n")
        else:
            h.write(str(expected)+"\n         ---------EVALUATE--------             "+str(correct)+"/"+str(len(prompt_array))+"\n")
         
        
# def confidence(output):
# 	m={}
# 	for tok in output.json()["completions"][0]["tokens"]:
# 		tok=tok["generatedToken"]
# 		m[tok["token"]] = tok["logprob"]
# 	print(m) 