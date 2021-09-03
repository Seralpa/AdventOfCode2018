with open("input22.txt") as f:
    depth=int(f.readline().strip()[7:])
    t1,t2=f.readline().strip()[8:].split(',')
    target=(int(t2),int(t1))

erosion_constant=20183
mapa=[]

#calculate erosion
for i in range(target[0]+1):
    mapa.append([])
    for j in range(target[1]+1):
        if (i,j)==(0,0) or (i,j)==target:#geo=0
            mapa[i].append((0+depth)%erosion_constant)
        elif i==0:
            mapa[i].append(((j*16807)+depth)%erosion_constant)
        elif j==0:
            mapa[i].append(((i*48271)+depth)%erosion_constant)
        else:
            mapa[i].append(((mapa[i-1][j]*mapa[i][j-1])+depth)%erosion_constant)

#calculate risc level and sum
suma=0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        mapa[i][j]=mapa[i][j]%3
        suma+=mapa[i][j]
print(suma)
