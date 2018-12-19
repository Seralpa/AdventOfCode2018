def cuentaX(mapa,x,pos):
    cont=0
    for i in range(pos[0]-1,pos[0]+2):
        for j in range(pos[1]-1,pos[1]+2):
            if pos!=(i,j) and i<len(mapa) and j<len(mapa[i]) and i>=0 and j>=0:
                if mapa[i][j]==x:
                    cont+=1
    return cont

with open("input18.txt") as f:
    mapa=[list(l.strip()) for l in f]

niteraciones=10
for _ in range(niteraciones):
    '''for m in mapa:
        print("".join(m))
    print('')'''
    updates=[]
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j]=='.':
                if cuentaX(mapa,'|',(i,j))>=3:
                    updates.append((i,j,'|'))
            elif mapa[i][j]=='|':
                if cuentaX(mapa,'#',(i,j))>=3:
                    updates.append((i,j,'#'))
            elif mapa[i][j]=='#':
                if cuentaX(mapa,'#',(i,j))<1 or cuentaX(mapa,'|',(i,j))<1:
                    updates.append((i,j,'.'))
    for u in updates:
        mapa[u[0]][u[1]]=u[2]
for m in mapa:
    print("".join(m))
contTree=0
contLumb=0
for l in mapa:
    for c in l:
        if c=='|':
            contTree+=1
        if c=='#':
            contLumb+=1
print(contLumb*contTree)