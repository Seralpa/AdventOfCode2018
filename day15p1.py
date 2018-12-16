import networkx as nx
from operator import itemgetter
def getUnitByPos(pos,units):
    for u in units:
        if pos==u.pos:
            return u

def generateGraph(mapa):
    gmapa=nx.Graph()
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j]=='.':
                if mapa[i-1][j]=='.':
                    gmapa.add_edge((i,j),(i-1,j))
                    #gmapa.add_edge((i-1,j),(i,j))
                if mapa[i][j-1]=='.':
                    gmapa.add_edge((i,j-1),(i,j))
                    #gmapa.add_edge((i,j),(i,j-1))
    return gmapa

def getNumUnitsByRaza(units):
    numE=0
    numG=0
    for u in units:
        if u.raza=='E':
            numE+=1
        else:
            numG+=1
    return (numE,numG)

def getHpSum(units):
    suma=0
    for u in units:
        suma+=u.hp
    return suma

class Unit:
    def __init__(self,pos,hp,atk,raza):
        self.pos=pos        #i,j
        self.hp=hp
        self.atk=atk
        self.raza=raza

    def isDead(self):
        return self.hp<1

    def attack(self,mapa,units,gmapa):
        enemigosCerca=[]
        #up
        if mapa[self.pos[0]-1][self.pos[1]] != '.' and mapa[self.pos[0]-1][self.pos[1]] != '#' and mapa[self.pos[0]-1][self.pos[1]] != self.raza:
            u=getUnitByPos((self.pos[0]-1,self.pos[1]),units)
            if not u.isDead():
                enemigosCerca.append(u)
        #left
        if mapa[self.pos[0]][self.pos[1]-1] != '.' and mapa[self.pos[0]][self.pos[1]-1] != '#' and mapa[self.pos[0]][self.pos[1]-1] != self.raza:
            u=getUnitByPos((self.pos[0],self.pos[1]-1),units)
            if not u.isDead():
                enemigosCerca.append(u)
        #right
        if mapa[self.pos[0]][self.pos[1]+1] != '.' and mapa[self.pos[0]][self.pos[1]+1] != '#' and mapa[self.pos[0]][self.pos[1]+1] != self.raza:
            u=getUnitByPos((self.pos[0],self.pos[1]+1),units)
            if not u.isDead():
                enemigosCerca.append(u)
            
        #down
        if mapa[self.pos[0]+1][self.pos[1]] != '.' and mapa[self.pos[0]+1][self.pos[1]] != '#' and mapa[self.pos[0]+1][self.pos[1]] != self.raza:
            u=getUnitByPos((self.pos[0]+1,self.pos[1]),units)
            if not u.isDead():
                enemigosCerca.append(u)
        if len(enemigosCerca)==0:
            return False
        
        #print("la unidad en "+str(self.pos)+" tiene enemigos cerca en estas posiciones "+str([e.pos for e in enemigosCerca]))
        enemigosCerca.sort(key = lambda hp:hp.hp)
        objetivo=enemigosCerca[0]
        
        objetivo.hp-=self.atk
        if objetivo.isDead():
            mapa[objetivo.pos[0]][objetivo.pos[1]]='.'
            #add objetivo.pos to gmapa
            #up
            if mapa[objetivo.pos[0]-1][objetivo.pos[1]] == '.':
                gmapa.add_edge(objetivo.pos,(objetivo.pos[0]-1,objetivo.pos[1]))
            #left
            if mapa[objetivo.pos[0]][objetivo.pos[1]-1] == '.':
                gmapa.add_edge(objetivo.pos,(objetivo.pos[0],objetivo.pos[1]-1))
            #right
            if mapa[objetivo.pos[0]][objetivo.pos[1]+1] == '.':
                gmapa.add_edge(objetivo.pos,(objetivo.pos[0],objetivo.pos[1]+1))
            #down
            if mapa[objetivo.pos[0]+1][objetivo.pos[1]] == '.':
                gmapa.add_edge(objetivo.pos,(objetivo.pos[0]+1,objetivo.pos[1]))
            
        

    def getEnemigos(self,units):
        return [u for u in units if u.raza!=self.raza]

    def move(self,mapa,units,gmapa):
        if len(self.getEnemigos(units))==0:
            return None
        #get objetivos
        objetivos=set()
        for e in self.getEnemigos(units):
            #up
            if mapa[e.pos[0]-1][e.pos[1]] == '.':
                objetivos.add((e.pos[0]-1,e.pos[1]))
            #left
            if mapa[e.pos[0]][e.pos[1]-1] == '.':
                objetivos.add((e.pos[0],e.pos[1]-1))
            #right
            if mapa[e.pos[0]][e.pos[1]+1] == '.':
                objetivos.add((e.pos[0],e.pos[1]+1))
            #down
            if mapa[e.pos[0]+1][e.pos[1]] == '.':
                objetivos.add((e.pos[0]+1,e.pos[1]))
        #sort objetivos
        objetivos=list(objetivos)
        objetivos.sort(key=itemgetter(1))
        objetivos.sort(key=itemgetter(0))

        #print("pos "+str(self.pos)+" objetivos "+str(objetivos))

        #calculate minimum paths to objetivos

        #add self.pos to gmapa
        #up
        if mapa[self.pos[0]-1][self.pos[1]] == '.':
            gmapa.add_edge(self.pos,(self.pos[0]-1,self.pos[1]))
        #left
        if mapa[self.pos[0]][self.pos[1]-1] == '.':
            gmapa.add_edge(self.pos,(self.pos[0],self.pos[1]-1))
        #right
        if mapa[self.pos[0]][self.pos[1]+1] == '.':
            gmapa.add_edge(self.pos,(self.pos[0],self.pos[1]+1))
        #down
        if mapa[self.pos[0]+1][self.pos[1]] == '.':
            gmapa.add_edge(self.pos,(self.pos[0]+1,self.pos[1]))

        minimum_paths=[]
        for o in objetivos:
            try:
                minimum_paths.append([p for p in nx.all_shortest_paths(gmapa,source=self.pos,target=o)])
            except:
                print(str(o)+" is not reachable from "+str(self.pos))
        
        if len(minimum_paths)==0:
            return None

        #select paths to objetivo with shortest minimum path
        minimum_paths.sort(key= lambda x:len(x[0]))
        minimum_paths=minimum_paths[0]
        
        #select move
        first_moves=list(set([p[1] for p in minimum_paths]))
        first_moves.sort(key = itemgetter(1))
        first_moves.sort(key = itemgetter(0))
        movimiento=first_moves[0]

        #realizar movimiento
        mapa[self.pos[0]][self.pos[1]]='.'
        mapa[movimiento[0]][movimiento[1]]=self.raza
        gmapa.remove_node(movimiento)
        self.pos=movimiento

mapa=[]
units=[]
with open("input15.txt","r") as f:
    mapa=f.readlines()
    for l in range(len(mapa)):
        mapa[l]=list(mapa[l].strip())
        for c in range(len(mapa[l])):
            if mapa[l][c]=='E':
                units.append(Unit((l,c),200,3,'E'))
            elif mapa[l][c]=='G':
                units.append(Unit((l,c),200,3,'G'))


gmapa=generateGraph(mapa)
#print(gmapa.nodes())
#print(gmapa.edges())
ronda=1
while ronda<2:
    #sort units in reading order
    units.sort(key = lambda j:j.pos[1])
    units.sort(key = lambda i:i.pos[0])
    for u in units:
        print(u.pos)
        if not u.isDead():
            if u.attack(mapa,units,gmapa)==False:
                u.move(mapa,units,gmapa)
                u.attack(mapa,units,gmapa)
    units=[u for u in units if not u.isDead()]
    numUnits=getNumUnitsByRaza(units)
    if numUnits[0]==0 or numUnits[1]==0:
        break
    print(ronda)
    ronda+=1
print(ronda*getHpSum(units))

for l in mapa:
    print("".join(l))

