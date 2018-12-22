import networkx as nx

with open("input22.txt") as f:
    depth=int(f.readline().strip()[7:])
    t1,t2=f.readline().strip()[8:].split(',')
    target=(int(t2),int(t1))

erosion_constant=20183
mapa=[]

#calculate erosion
for i in range(target[0]+100):
    mapa.append([])
    for j in range(target[1]+100):
        if (i,j)==(0,0) or (i,j)==target:#geo=0
            mapa[i].append((0+depth)%erosion_constant)
        elif i==0:
            mapa[i].append(((j*16807)+depth)%erosion_constant)
        elif j==0:
            mapa[i].append(((i*48271)+depth)%erosion_constant)
        else:
            mapa[i].append(((mapa[i-1][j]*mapa[i][j-1])+depth)%erosion_constant)

#calculate risc level
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        mapa[i][j]=mapa[i][j]%3

gmapa=nx.Graph()
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]==0:#rock
            gmapa.add_edge((i,j,'T'),(i,j,'C'),w=7)
        elif mapa[i][j]==1:#wet
            gmapa.add_edge((i,j,'N'),(i,j,'C'),w=7)
        elif mapa[i][j]==2:#narrow
            gmapa.add_edge((i,j,'N'),(i,j,'T'),w=7)

        if i>0:
            if mapa[i][j]==0:#rock
                if mapa[i-1][j]==0:#rock
                    gmapa.add_edge((i,j,'T'),(i-1,j,'T'),w=1)
                    gmapa.add_edge((i,j,'C'),(i-1,j,'C'),w=1)
                elif mapa[i-1][j]==1:#wet
                    gmapa.add_edge((i,j,'C'),(i-1,j,'C'),w=1)
                elif mapa[i-1][j]==2:#narrow
                    gmapa.add_edge((i,j,'T'),(i-1,j,'T'),w=1)
            elif mapa[i][j]==1:#wet
                if mapa[i-1][j]==0:#rock
                    gmapa.add_edge((i,j,'C'),(i-1,j,'C'),w=1)
                elif mapa[i-1][j]==1:#wet
                    gmapa.add_edge((i,j,'C'),(i-1,j,'C'),w=1)
                    gmapa.add_edge((i,j,'N'),(i-1,j,'N'),w=1)
                elif mapa[i-1][j]==2:#narrow
                    gmapa.add_edge((i,j,'N'),(i-1,j,'N'),w=1)
            elif mapa[i][j]==2:#narrow
                if mapa[i-1][j]==0:#rock
                    gmapa.add_edge((i,j,'T'),(i-1,j,'T'),w=1)
                elif mapa[i-1][j]==1:#wet
                    gmapa.add_edge((i,j,'N'),(i-1,j,'N'),w=1)
                elif mapa[i-1][j]==2:#narrow
                    gmapa.add_edge((i,j,'N'),(i-1,j,'N'),w=1)
                    gmapa.add_edge((i,j,'T'),(i-1,j,'T'),w=1)
        if j>0:
            if mapa[i][j]==0:#rock
                if mapa[i][j-1]==0:#rock
                    gmapa.add_edge((i,j,'T'),(i,j-1,'T'),w=1)
                    gmapa.add_edge((i,j,'C'),(i,j-1,'C'),w=1)
                elif mapa[i][j-1]==1:#wet
                    gmapa.add_edge((i,j,'C'),(i,j-1,'C'),w=1)
                elif mapa[i][j-1]==2:#narrow
                    gmapa.add_edge((i,j,'T'),(i,j-1,'T'),w=1)
            elif mapa[i][j]==1:#wet
                if mapa[i][j-1]==0:#rock
                    gmapa.add_edge((i,j,'C'),(i,j-1,'C'),w=1)
                elif mapa[i][j-1]==1:#wet
                    gmapa.add_edge((i,j,'C'),(i,j-1,'C'),w=1)
                    gmapa.add_edge((i,j,'N'),(i,j-1,'N'),w=1)
                elif mapa[i][j-1]==2:#narrow
                    gmapa.add_edge((i,j,'N'),(i,j-1,'N'),w=1)
            elif mapa[i][j]==2:#narrow
                if mapa[i][j-1]==0:#rock
                    gmapa.add_edge((i,j,'T'),(i,j-1,'T'),w=1)
                elif mapa[i][j-1]==1:#wet
                    gmapa.add_edge((i,j,'N'),(i,j-1,'N'),w=1)
                elif mapa[i][j-1]==2:#narrow
                    gmapa.add_edge((i,j,'N'),(i,j-1,'N'),w=1)
                    gmapa.add_edge((i,j,'T'),(i,j-1,'T'),w=1)

print(nx.shortest_path_length(gmapa,(0,0,'T'),(target[0],target[1],'T'),weight='w'))