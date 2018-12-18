import re
from operator import itemgetter
rango=re.compile(r"[a-z]=(\d+)..(\d+)")

mapa=[]
muros=set()
with open("inputTest.txt","r") as f:
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

for i in range(maxy+1):
    mapa.append([])
    for j in range(maxx+1):
        mapa[i].append('.')

for m in muros:
    mapa[m[0]][m[1]]='#'

mapa[0][500]='|'
contAnterior=0
for _ in range(1):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j]=='|':
                if mapa[i+1][j]=='.':
                    mapa[i+1][j]='|'
                elif mapa[i+1][j]!='|':
                    if mapa[i][j-1]=='.':
                        mapa[i][j-1]='|'
                    if mapa[i][j+1]=='.':
                        mapa[i][j+1]='|'
            elif mapa[i][j]=='#':#TODO la deteccion de muros no funciona, detecta estancamiento cuando hay agua fluyendo
                print("muro "+str((i,j)))
                hayAgua=False
                for j1 in range(j+1,len(mapa[i])):
                    if mapa[i][j1]=='|' and not hayAgua:
                        hayAgua=True
                    if hayAgua:
                        mapa[i][j1]='~'
                    if mapa[i][j1]=='#':
                        print("finmuro "+str((i,j1)))
                        break
    cont=0        
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if i>=miny and i<=maxy:
                if mapa[i][j]=='|' or mapa[i][j]=='~':
                    cont+=1
    '''if cont==contAnterior:
        break
    contAnterior=cont'''
for m in mapa:
    print("".join(m))