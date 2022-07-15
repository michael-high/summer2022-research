import os,glob
for filename in glob.glob(os.path.join("C:\CS\SUM2022\SUM2022-github\data\\1-current-set", '*.txt')):
  with open(filename, 'r') as f:
    counter=0
    for line in f:
        if "###" in line:
            counter+=1
    file=str(filename)
    name=file.split("current-set")
    print(name[1]+": "+str(counter))