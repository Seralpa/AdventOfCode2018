
lineas=[]
doses=0
treses=0
with open("input2.txt","r") as f:
    lineas=f.readlines()

for line in lineas:
    repiteDos=False
    repiteTres=False
    for l in line:
        count=line.count(l)
        if count==2:
            repiteDos=True
        if count==3:
            repiteTres=True
        if repiteDos and repiteTres:
            break
        line.replace(l,"")
    if repiteDos:
        doses+=1
    if repiteTres:
        treses+=1

print(doses*treses)