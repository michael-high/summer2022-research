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
        with open()
