cadena=""

with open("input5.txt","r") as f:
    cadena=f.readline().strip()

cadena=list(cadena)
modified=True
while modified:
    modified=False
    for c in range(len(cadena)-1):
        if abs(ord(cadena[c])-ord(cadena[c+1]))==32:
            del cadena[c:c+2]
            modified=True
            break
print(len(cadena))