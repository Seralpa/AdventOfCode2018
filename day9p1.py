import re
data=re.compile(r"([0-9]+) players; last marble is worth ([0-9]+) points")
jugadores=[]
circulo=[0,1]

with open("input9.txt","r") as f:
    linea=f.readline().strip()
    numJugadores=int(data.match(linea).group(1))
    numMarbles=int(data.match(linea).group(2))

for _ in range(numJugadores):
    jugadores.append(0)
current=1
for i in range(2,numMarbles+1):
    if i%23 == 0:
        jugadores[i%len(jugadores)-1]+=i
        jugadores[i%len(jugadores)-1]+=circulo.pop(current-7)
        current-=7

    else:
        current=(current+2)%len(circulo)
        circulo.insert(current,i)

print(max(jugadores))