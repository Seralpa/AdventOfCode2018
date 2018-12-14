
def gira(direccion,giro):
    if giro==1:
        return direccion
    if giro==0:#left
        if direccion==(0,1):
            direccion=(-1,0)
        elif direccion==(0,-1):
            direccion=(1,0)
        elif direccion==(1,0):
            direccion=(0,1)
        elif direccion==(-1,0):
            direccion=(0,-1)
        return direccion
    elif giro==2:#right
        if direccion==(0,1):
            direccion=(1,0)
        elif direccion==(0,-1):
            direccion=(-1,0)
        elif direccion==(1,0):
            direccion=(0,-1)
        elif direccion==(-1,0):
            direccion=(0,1)
        return direccion
    else:
        raise ValueError("gilipollas")

class Coche:
    def __init__(self,pos,direccion):
        self.pos=pos
        self.dir=direccion  #formato (i,j) i positivo abajo j positivo derecha
        self.nextIntesect=0 #0->left 1->straight 2->right

    def avanza(self,mapa):
        if mapa[self.pos[0]][self.pos[1]]=='+':
            self.dir=gira(self.dir,self.nextIntesect)
            self.nextIntesect=(self.nextIntesect+1)%3
        elif mapa[self.pos[0]][self.pos[1]]=='/':
            if self.dir==(-1,0):
                self.dir=(0,1)
            elif self.dir==(0,-1):
                self.dir=(1,0)
            elif self.dir==(1,0):
                self.dir=(0,-1)
            elif self.dir==(0,1):
                self.dir=(-1,0)
        elif mapa[self.pos[0]][self.pos[1]]=='\\':
            if self.dir==(-1,0):
                self.dir=(0,-1)
            elif self.dir==(0,-1):
                self.dir=(-1,0)
            elif self.dir==(1,0):
                self.dir=(0,1)
            elif self.dir==(0,1):
                self.dir=(1,0)
        self.pos=(self.pos[0]+self.dir[0],self.pos[1]+self.dir[1])
            
    def haChocado(self,coches):
        for c in coches:
            if c!=self and c.pos==self.pos:
                return True
        return False

mapa=[]
coches=[]
with open("input13.txt","r") as f:
    for l in f:
        mapa.append(list(l.replace('\n',"")))

#quitar coches
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        if mapa[i][j]=='v':
            mapa[i][j]='|'
            coches.append(Coche((i,j),(1,0)))
        if mapa[i][j]=='^':
            mapa[i][j]='|'
            coches.append(Coche((i,j),(-1,0)))
        if mapa[i][j]=='<':
            mapa[i][j]='-'
            coches.append(Coche((i,j),(0,-1)))
        if mapa[i][j]=='>':
            mapa[i][j]='-'
            coches.append(Coche((i,j),(0,1)))

while True:
    '''for l in mapa:
        print("".join(l))'''
    for c in coches:
        #print(c.pos)
        c.avanza(mapa)
        if c.haChocado(coches):
            print(c.pos)
            raise ValueError("catapum")
    coches.sort(key = lambda j:j.pos[1])
    coches.sort(key = lambda i:i.pos[0])
    #input("continua")