import operator
tamMax=300
serial=2568
cuadrantes={}

def ijtam(i,j,tam):
    if (i,j,tam) in cuadrantes:
        return cuadrantes[(i,j,tam)]
    if tam%2==0:
        suma=ijtam(i,j,tam/2)+ijtam(i,j+tam/2,tam/2)+ijtam(i+tam/2,j,tam/2)+ijtam(i+tam/2,j+tam/2,tam/2)
    elif tam==1:
        suma=getPower(i,j)
    else:
        suma=ijtam(i,j,tam-1)
        for a in range(tam):
            suma+=ijtam(i+a,j+tam-1,1)
        for a in range(tam-1):
            suma+=ijtam(i+tam-1,j+a,1)
    cuadrantes[(i,j,tam)]=suma
    return suma

def getPower(i,j):
    power=(((j+1+10)*(i+1))+serial)*(j+1+10)
    power=(power%1000)//100
    return power-5

for tam in range(1,tamMax-1):
    print(tam)
    for i in range(tamMax-tam+1):
        for j in range(tamMax-tam+1):
            ijtam(i,j,tam)
        
print(max(list(cuadrantes.items()),key=operator.itemgetter(1)))