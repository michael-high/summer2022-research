filename="tollens"
input=""
with open(f"C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\inferences\\{filename}.txt","r") as f:
    input=f.read().replace("\n","")
string=str(input)
exList=string.split("###")

with open(f"C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\inferences\conversion\single-inference-prompt\\{filename}.jsonl","a") as f:
    for i in range(0, len(exList)-1):
        ex=exList[i].split("Proof:")
        asumps=ex[0].split("Assumption")
        prompt=""
        for i in range(1,len(asumps)):
            prompt+=('Assumption'+asumps[i]+'\\n')
        out='{"prompt": "'+prompt+'", "completion": "Proof:'+ex[1]+'"}\n'
        f.write(out)

        