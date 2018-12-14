import sys
resultados=[]
resultado=0
lineas=[]
with open("input.txt","r") as f:
    for line in f:
        lineas.append(int(line))
#print(lineas)
while True:
    for n in lineas:
        if resultado in resultados:
            print(resultado)
            #print(resultados)
            sys.exit()
        resultados.append(resultado)
        resultado+=n