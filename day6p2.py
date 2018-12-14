from operator import itemgetter

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
        totalDist=0
        for p in listapuntos:
            totalDist+=distancia(p,(x,y))
        if totalDist<10000:    
            matrix[y].append(1)
        else:
            matrix[y].append(0)

matrix=[j for sub in matrix for j in sub]
print(matrix.count(1))


        