import re
import operator
data=re.compile(r"position=< ?(-?[0-9]+),  ?(-?[0-9]+)> velocity=< ?(-?[0-9]+),  ?(-?[0-9]+)>")

'''def crearTab(pos,minx,maxx,miny,maxy):
    tab=[]
    for i in range(maxy-miny+1):
        tab.append([])
        for j in range(maxx-minx+1):
            tab[i].append('#' if (j,i) in pos else '.')
    return tab'''
class Punto:
    def __init__(self,pos,vel):
        self.pos=pos
        self.vel=vel
    
    def mueve(self):
        self.pos=(self.pos[0]+self.vel[0],self.pos[1]+self.vel[1])


def printPos(puntos,minx,maxx):
    pAnterior=puntos[0]
    for p in puntos:
        if p==puntos[0]:
            for _ in range(p.pos[0]-minx):
                print('.',end='')
            print('#',end='')
            continue
        if p.pos==pAnterior.pos:
            #print("rep",end='')
            continue
        if p.pos[1]==pAnterior.pos[1]:
            for _ in range(p.pos[0]-pAnterior.pos[0]-1):
                print('.',end='')
        else:
            
            for _ in range(maxx-pAnterior.pos[0]):
                print('.',end='')
            for _ in range(p.pos[1]-pAnterior.pos[1]):
                print('')
            for _ in range(p.pos[0]-minx):
                print('.',end='')
        print('#',end='')
        pAnterior=p
    print('')


puntos=[]
with open("input10.txt","r") as f:
    for l in f:
        matcher=data.match(l)
        puntos.append(Punto((int(matcher.group(1)),int(matcher.group(2))),(int(matcher.group(3)),int(matcher.group(4)))))

time=0
while True:
    minx=min(puntos,key=lambda x:x.pos[0]).pos[0]
    maxx=max(puntos,key=lambda x:x.pos[0]).pos[0]
    if maxx-minx<100:
        puntos.sort(key = lambda x:x.pos[0])
        puntos.sort(key = lambda y:y.pos[1])
        '''tab=crearTab(pos,minx,maxx,miny,maxy)
        for i in tab:
            print(i)'''
        for p in puntos:
            print(p.pos,end='')
        print('')
        printPos(puntos,minx,maxx)
        print(time)
        input("cualquier tecla para seguir")
    for p in puntos:
        p.mueve()
    time+=1
