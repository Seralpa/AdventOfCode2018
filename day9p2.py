import re

class Nodo:
    def __init__(self,dato,anterior,siguiente):
        self.dato=dato
        self.anterior=anterior
        self.siguiente=siguiente

    def insertarDespues(self,dato):
        insercion=Nodo(dato,self,self.siguiente)
        self.siguiente.anterior=insercion
        self.siguiente=insercion

    def eliminarAntes(self):
        dosAtras=self.anterior.anterior
        self.anterior=dosAtras
        dosAtras.siguiente=self


data=re.compile(r"([0-9]+) players; last marble is worth ([0-9]+) points")
jugadores=[]

with open("input9.txt","r") as f:
    linea=f.readline().strip()
    numJugadores=int(data.match(linea).group(1))
    numMarbles=int(data.match(linea).group(2))

for _ in range(numJugadores):
    jugadores.append(0)

inicio=Nodo(0,None,None)
current=Nodo(1,inicio,inicio)
inicio.siguiente=current
inicio.anterior=current
for i in range(2,numMarbles+1):
    if i%23 == 0:
        jugadores[i%len(jugadores)-1]+=i
        nodo7atras=current.anterior.anterior.anterior.anterior.anterior.anterior.anterior
        jugadores[i%len(jugadores)-1]+=nodo7atras.dato
        current=nodo7atras.siguiente
        current.eliminarAntes()

    else:
        current.siguiente.insertarDespues(i)
        current=current.siguiente.siguiente

print(max(jugadores))