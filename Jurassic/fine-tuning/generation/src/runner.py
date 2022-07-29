import openai
import requests
import json

class runner():
    experiments = []
    path = ""
    openAIKey = ""
    AI21Key = ""
    models = {
        "openai":[],
        "ai21":[]
    }
    
    def __init__(self,experiments=[],path="./",openAIKey ="", AI21Key = ""):
        self.experiments = experiments
        self.path = path
        self.openAIKey = openAIKey
        self.AI21Key = AI21Key
    
    def add(self,*args):
        for i in args:
            self.experiments.append(i)

    def setOpenAIKey(self,key):
        self.openAIKey = key
    
    def setAI21Key(self,key):
        self.AI21Key = key
    
    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path
    
    def runOpenAI(self,model,experiment):
        assert self.openAIKey != "", "Please add OpenAI key with setOpenAIKey method"
        openai.api_key= self.openAIKey
        out=openai.Completion.create(engine=model, temperature=0, prompt=experiment, max_tokens=1024, stop="\n")
        out = out["choices"][0]["text"] + "\n"
        return out

    
    def runAI21(self,model,experiment):
        assert self.AI21Key != "", "Please add AI21 key with setAI21Key method"
        out = requests.post(
            f"https://api.ai21.com/studio/v1/{model}/complete",
            headers={"Authorization": self.AI21Key},
            json={
                "prompt": experiment, 
                "numResults": 1, 
                "maxTokens": 1024, 
                "stopSequences": ["\n"],
                "topKReturn": 0,
                "temperature": 0.0
            }    
        )
        out = out.json()["completions"][0]["data"]["text"] +"\n"
        return out
        

    def run(self,provider,model):
        assert provider == "openAI" or provider == "AI21", "Provider has to be openAI or AI21"
        n = 1
        for experiment in self.experiments[0]:
            a = f"----------------------------------EXPERIMENT NUMBER {n}--------------MODEL {model}--------------------\n"
            with open(self.path,"a") as f:
                f.write(a)
                f.write(experiment.getExp())
                if provider == "openAI":
                    f.write(self.runOpenAI(model,experiment.getExp()))
                elif provider == "AI21":
                    f.write(self.runAI21(model,experiment.getExp()))
                f.write(f"Troof: {experiment.getTroof()}")
            n += 1

    def rumMulti(self):
        n = 1
        for experiment in self.experiments[0]:
            a = f"----------------------------------EXPERIMENT NUMBER {n}--------------MODEL j1-jumbo--------------------\n"
            with open(self.path,"a") as f:
                f.write(a)
                f.write(experiment.getExp())
                out = requests.post(
                "https://api.ai21.com/studio/v1/j1-jumbo/complete",
                headers={"Authorization": self.AI21Key},
                json={
                    "prompt": experiment.getExp(), 
                    "numResults": 1, 
                    "maxTokens": 1024, 
                    "stopSequences":["###"],
                    "topKReturn": 0,
                    "temperature": 0.0
            }    
            )
                out = out.json()["completions"][0]["data"]["text"] +"\n"
                f.write(out)
                f.write("TROOF: \n")
                f.write(experiment.getTroof())
            n += 1
    
    def runModels(self):
        n = 1
        for experiment in self.experiments[0]:
            a = f"----------------------------------EXPERIMENT NUMBER {n}--------------MODEL J1-Jumbo--------------------\n"
            b = f"----------------------------------EXPERIMENT NUMBER {n}--------------MODEL GPT-3--------------------\n"
            with open(self.path,"a") as f:
                f.write(a)
                f.write(experiment.getExp())
                f.write(self.runAI21("j1-jumbo",experiment.getExp()))
                f.write(f"Troof: {experiment.getTroof()}")
                f.write(b)
                f.write(experiment.getExp())
                f.write(self.runOpenAI("text-davinci-002",experiment.getExp()))
                f.write(f"Troof: {experiment.getTroof()}")
            n += 1

    def runTrials(self):
        n = 1
        results = {}
        for experiment in self.experiments[0]:
            a = f"----------------------------------EXPERIMENT NUMBER {n}--------------MODEL J1-Jumbo--------------------\n"
            res = self.runAI21("j1-jumbo",experiment.getExp())
            with open(self.path,"a") as f:
                f.write(a)
                f.write(experiment.getExp())
                f.write(res)
                f.write(f"Troof: {experiment.getTroof()}")
            if res in results:
                results[res] += 1
            else:
                results[res] = 1

            
        with open(self.path,"a") as f:
            f.write("-----------------------------RESULTS---------------------------\n")
            f.write(json.dumps(results))
