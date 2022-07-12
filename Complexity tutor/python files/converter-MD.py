ass = {}
req = {}
with open("C:\CS\SUM2022\complexity tutor\MuddyDog.py") as f:
    for line in f:
        if "= ProofItem" in line:
            x=line.split(" = ProofItem")
            y=x[1]
            y=y.replace("(","")
            z=y.split(")")
            ass[x[0]]=z[0]
        if ".Requirements.Add" in line:
            a=line.split(".Requirements.Add")
            b=a[1]
            b=b.replace("(","")
            c=b.split(")")
            if a[0] in req:
                req[a[0]].append(ass[c[0]])    
            else: 
                req[a[0]]=[ass[c[0]]]
        if ".isAss" in line:
            g=line.split(".isAss")
            req[g[0]]="None"
        if ".isWrong" in line:
            itback=line.split(".isWrong")
            ass.pop(itback[0])
out=""
# for assertion in ass:
#     for x in req:
#         if x==assertion:
#             out+="R: "+str(req[assertion])+"\n"
#     out+="A: "+ass[assertion]+"\n\n"
for assertion in ass:
    if assertion not in req:
        continue
    if req[assertion]=="None":
            continue
    for x in req:
        if x==assertion:
            out+="R:"
            if "Biscuit" in ass[assertion]:
                out+='"Biscuit is a dog" ; '
            if "Cardie" in ass[assertion]:
                out+='"Cardie is a dog" ; '
            if "Duncan" in ass[assertion]:
                out+='"Duncan is a dog" ; '
            if type(req[assertion])==list:
                if len(req[assertion])!=1:                         
                    for i in range(0, len(req[assertion])):
                        #print(i, "\n", req[assertion] , "\n", assertion, type(assertion), "\n", assertion[0], type(assertion[0]))                                                
                        out+=req[assertion][i]                                              
                        if  i != len(req[assertion])-1:                                                       
                            out += " ; "                                                   
                    out+= "\n"                                                       
                else:
                    for x in req[assertion]:
                        out+=x+"\n"
            else:
                out+=(req[assertion]+"\n")
    out+="A:"+ass[assertion]+"\n\n"

with open(".\MD-conv.txt","w") as q:
    q.write(out)