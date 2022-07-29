from .ds import data, example, multiExp

def parse(path):
    with open(path,"r") as f:
        d = data()
        ex = example()
        for line in f:
            if "Assumption" in line:
                ex.addAssumption(line)
                continue
            if "Proof" in line:
                ex.addProof(line)
                continue
            if "###" in line:
                d.add(ex)
                ex = example()
                continue
    return d

def parseMulti(path):
    with open(path,"r") as f:
        d = data()
        ex = multiExp()
        for line in f:
            if "Assumption" in line:
                ex.addAssumption(line)
            elif "###" in line:
                d.add(ex)
                ex = multiExp()
            else:
                ex.addProofstr(line)
                temp = line.split(" ",1)
                ex.addProof(temp[0],temp[1])
    return d

def removeCause(path):
    with open(path,"r") as f:
        lines = f.readlines()
    with open(path,"w") as f:
        flag = False
        for line in lines:
            if "cause" not in line and not flag:
                f.write(line)
            elif "cause" in line:
                flag = True
            elif flag and "###" in line:
                flag = False