import re
lineaInstr=re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

instrucciones=[]
tareas=""
with open("input7.txt","r") as f:
    for l in f:
        instrucciones.append((lineaInstr.match(l).group(1),lineaInstr.match(l).group(2)))
        
while len(abc)>0:
    aunNo=[i[1] for i in instrucciones]
    for a in abc:
        if not a in aunNo:
            tareas+=a
            abc=abc.replace(a,"")
            instrucciones=[i for i in instrucciones if i[0]!=a]
            break
print(tareas)