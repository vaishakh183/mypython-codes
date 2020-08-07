a=[]
with open("epoch","r") as f:
    for i in f.readlines():
        b=i.split()
        print(b[16].split("[")[1].strip(","))