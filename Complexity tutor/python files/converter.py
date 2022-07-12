# f=open("C:\CS\SUM2022\complexity tutor\PizzaProblem.py", "r")
#f=open(r".\PizzaProblem.txt", "r")
# print(f.read())

#print("\\g")
ass = {}
req = {}
with open("C:\CS\SUM2022\complexity tutor\PizzaProblem.py") as f:
    for line in f:
        if "= ProofItem" in line:
            x=line.split(" = ProofItem")
            #print(x)
            y=x[1]
            y=y.replace("(","")
            z=y.split(")")
            
            ass[x[0]]=z[0]
        if ".Requirements.Add" in line:
            a=line.split(".Requirements.Add")
            b=a[1]
            b=b.replace("(","")
            c=b.split(")")

            # b=b.replace(")","\\")
            # print(b)
            # b=b.replace("\n","")
            # #b=b.replace("n","")
            # print(b)
            req[a[0]]=ass[c[0]]
        # if ".isAssumption = True" in line:
        #     l=line.split(".is")
        #     ass[l[0]]=
# print(ass, "\n\n") 
# print(req, "\n\n")

# for reqs in req:
#     print(req[reqs])

# print("\n\n")



for assertion in ass:
    if assertion in req:
        print("R:",req[assertion])
    else:
        print("R: None")
    print("A:", ass[assertion], "\n")
        #for each in req[assertion]:
            #print(req[assertion])
        