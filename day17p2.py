import re
from operator import itemgetter
rango=re.compile(r"[a-z]=(\d+)..(\d+)")

mapa=[]
muros=set()
with open("input17.txt","r") as f:
    for l in f:
        c1,c2=l.strip().split(", ")
        if c1[0]=='x':
            j=int(c1[2:])
            if rango.match(c2)!=None:
                for i in range(int(rango.match(c2).group(1)),int(rango.match(c2).group(2))+1):
                    muros.add((i,j))
            else:
                i=int(c2[2:])
                muros.add((i,j))
        else:
            i=int(c1[2:])
            if rango.match(c2)!=None:
                for j in range(int(rango.match(c2).group(1)),int(rango.match(c2).group(2))+1):
                    muros.add((i,j))
            else:
                j=int(c2[2:])
                muros.add((i,j))
muros=list(muros)
miny=min(muros,key=itemgetter(0))[0]
maxy=max(muros,key=itemgetter(0))[0]
maxx=max(muros,key=itemgetter(1))[1]+1

for i in range(maxy+2):
    mapa.append([])
    for j in range(maxx+1):
        mapa[i].append('.')

for m in muros:
    mapa[m[0]][m[1]]='#'

mapa[0][500]='|'
contAnterior=0
while True:
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j]=='|' and i<len(mapa)-1:
                if mapa[i+1][j]=='.':
                    mapa[i+1][j]='|'
                elif mapa[i+1][j]!='|':
                    if mapa[i][j-1]=='.':
                        mapa[i][j-1]='|'
                    if mapa[i][j+1]=='.':
                        mapa[i][j+1]='|'
            elif mapa[i][j]=='#':
                hayAgua=False
                estancar=False
                for j1 in range(j+1,len(mapa[i])):
                    if not hayAgua and mapa[i][j1]=='|':
                        hayAgua=True
                    if mapa[i+1][j1]=='.' or mapa[i+1][j1]=='|' or mapa[i][j1]=='~':
                        break
                    if mapa[i][j1]=='#':
                        estancar=True
                        finj=j1
                        break
                #estancar el agua
                if hayAgua and estancar:
                    for j2 in range(j+1,finj):
                        mapa[i][j2]='~'
    cont=0        
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if i>=miny and i<=maxy:
                if mapa[i][j]=='|' or mapa[i][j]=='~':
                    cont+=1
    print(cont)
    if cont==contAnterior:
        break
    contAnterior=cont
print("fin")
contestanco=0
for i in mapa:
    for j in i:
        if j=='~':
            contestanco+=1
print(contestanco)
