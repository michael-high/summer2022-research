import requests
import json

class uploader():
    experiments=[]

    def __init__(self, experiments):
        self.experiments=experiments
    
    def add(self,*args):
        for i in args:
            self.experiments.append(i)
    
    def convert(self):
        with open("C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\generation\src\\temp.txt", "w") as f:
            f.write("")

        for exp in self.experiments:
            with open("C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\generation\src\\temp.txt", "a") as f:
                f.write("00000")
                f.write(exp.getExp())
                f.write(f"Troof: {exp.getTroof()}")
        with open("C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\generation\src\\temp.txt", "r") as f:
            raw=f.read().replace("\n","")
        string=str(raw)
        promptList=string.split("00000")

        with open("C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\generation\src\\temp.jsonl", "w") as f:
            for i in range(1, len(promptList)):
                prompt=promptList[i].split("Proof:Troof:")
                completion=prompt[1]
                prompt=prompt[0]
                exas=prompt.split("###")
                p=""
                for i in range(0, len(exas)-1):
                    a=exas[i].split("Proof:")
                    Proof=a[1]
                    assumps=a[0].split("Assumption")
                    p+=('Assumption'+assumps[1]+'\\n'+'Assumption'+assumps[2]+'\\n'+'Proof:'+Proof+'\\n')
                last=exas[len(exas)-1]
                print(last)
                assumps=last.split("Assumption")
                for i in range(1,len(assumps)):
                     p+=('Assumption'+assumps[i]+'\\n')
                out='{"prompt": "'+p+'", "completion": "Proof:'+completion+'"}\n'
                f.write(out)