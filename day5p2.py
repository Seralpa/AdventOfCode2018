def elimina(cadena,letra):
    cad=[value for value in cadena if value != letra]
    cad=[value for value in cad if value != letra.upper()]
    return cad

cadenaTotal=""
abc="abcdefghijklmnopqrstuvwxyz"
with open("input5.txt","r") as f:
    cadenaTotal=f.readline().strip()
listaVals=[]
cadenaTotal=list(cadenaTotal)
for char in abc:
    cadena=elimina(cadenaTotal,char)
    modified=True
    while modified:
        modified=False
        for c in range(len(cadena)-1):
            if abs(ord(cadena[c])-ord(cadena[c+1]))==32:
                del cadena[c:c+2]
                modified=True
                break
    listaVals.append(len(cadena))
print(min(listaVals))