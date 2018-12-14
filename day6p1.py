from operator import itemgetter
from collections import Counter

def distancia(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

matrix=[]
listapuntos=[]
with open("input6.txt","r") as f:
    for l in f:
        line=l.split(", ")
        listapuntos.append((int(line[0]),int(line[1])))

maxx=max(listapuntos,key=itemgetter(0))[0]+1
maxy=max(listapuntos,key=itemgetter(1))[1]+1

for y in range(maxy):
    matrix.append([])
    for x in range(maxx):
        minDistance=1000
        punto=-1
        for p in range(len(listapuntos)):
            dist=distancia(listapuntos[p],(x,y))
            if dist==minDistance:
                punto=-1
            if minDistance>dist:
                minDistance=dist
                punto=p
        matrix[y].append(punto)

inf=set([])
#upper and lower
for x in range(len(matrix[0])):
    inf.add(matrix[0][x])
    inf.add(matrix[len(matrix)-1][x])

for y in range(len(matrix)):
    inf.add(matrix[y][0])
    inf.add(matrix[y][len(matrix[0])-1])

matrix=[j for sub in matrix for j in sub]

cnt=Counter(matrix)
for p in cnt.most_common():
    if not p[0] in inf:
        print(p)
        break

        