out=""
with open("C:\CS\SUM2022\MD-conv.txt", "r") as file:
    for line in file:
        x=line
        if '"Biscuit is a Dog"' in x:
            x.replace('"Biscuit is a Dog" ; ',"")
        if '"Cardie is a Dog"' in x:
            x.replace('"Cardie is a Dog" ; ',"")
        if '"Duncan is a Dog"' in x:
            x.replace('"Duncan is a Dog" ; ',"")
        if "Cardie" in x:
            x.replace("Cardie the dog","Cardie")
        if "Duncan" in x:
            x.replace("Duncan","Duncan the dog")
        if "Biscuit" in x:
            x.replace("Biscuit","Biscuit the dog")
        out+=x
with open("C:\CS\SUM2022\MD1-conv.txt", "w") as h:
    h.write(out)