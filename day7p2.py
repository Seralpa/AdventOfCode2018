import re
lineaInstr=re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

nworkers=5
def tareasCerradas(instrucciones,hechas):
    instr=instrucciones
    for t in hechas:
        instr=[i for i in instr if i[0]!=t]
    return [i[1] for i in instr]

def tareasAbiertas(instrucciones,hechas,asignadas):
    aunNo=tareasCerradas(instrucciones,hechas)
    toDo=[t for t in abc if not t in hechas and not t in aunNo]
    toDo=list(set(toDo).difference(asignadas))
    return toDo

def getDuration(tarea):
    return (ord(tarea)-ord('A'))+60

instrucciones=[]
hechas=[]
asignadas=[]

with open("input7.txt","r") as f:
    for l in f:
        instrucciones.append((lineaInstr.match(l).group(1),lineaInstr.match(l).group(2)))
        

tabla=[]
abiertas=tareasAbiertas(instrucciones,hechas,asignadas)
timestamp=[None for _ in range(nworkers)]
for i in range(nworkers):
    if i<len(abiertas):
        timestamp[i]=(abiertas[i],getDuration(abiertas[i]))
        asignadas.append(abiertas[i])
tabla.append(timestamp)

time=0
while True:
    time+=1
    timestamp=[None for _ in range(nworkers)]
    for i in range(nworkers):
        if tabla[time-1][i]!=None:
            if tabla[time-1][i][1]!=0:      #el trabajador ya tenia una tarea sin acabar
                timestamp[i]=(tabla[time-1][i][0],tabla[time-1][i][1]-1)
            else:                           #el trabajador ha acabado su tarea
                hechas.append(tabla[time-1][i][0])
                asignadas.remove(tabla[time-1][i][0])
    abiertas=tareasAbiertas(instrucciones,hechas,asignadas)
    for i in range(nworkers):
        if timestamp[i]==None and 0<len(abiertas):
            timestamp[i]=(abiertas[0],getDuration(abiertas[0]))
            asignadas.append(abiertas[0])
            abiertas.remove(abiertas[0])
    if len(hechas)==len(abc):
        break
    tabla.append(timestamp)

print(time)

'''while len(abc)>0:
    aunNo=[i[1] for i in instrucciones]
    for a in abc:
        if not a in aunNo:
            tareas+=a
            abc=abc.replace(a,"")
            instrucciones=[i for i in instrucciones if i[0]!=a]
            break
print(tareas)'''