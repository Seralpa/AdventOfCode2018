class Nodo:
    def __init__(self,padre,numHijos,numData):
        


        self.padre=padre
        self.numhijos=numHijos
        self.numData=numData
        self.hijos=[]
        self.data=[]
    
    def addHijos(self,datos):
        for i in range(self.numhijos):
            hijo=Nodo(self,datos.pop(0),datos.pop(0))
            hijo.addHijos(datos)
            self.hijos.append(hijo)
        self.addData(datos)

    def addData(self,datos):
        for _ in range(self.numData):
            self.data.append(datos.pop(0))

    def __str__(self):
        print("\nData= "+str(self.data)+"\nHijos= ")
        for h in self.hijos:
            print("hijo")
            print(h)
        if len(self.hijos)==0:
            print("[]")
        return "----------fin-----------"
    
    def sumData(self):
        suma=sum(self.data)
        for h in self.hijos:
            suma+=h.sumData()
        return suma

    def getValue(self):
        if len(self.hijos)==0:
            return sum(self.data)
        suma=0
        for d in self.data:
            if d<=len(self.hijos):
                suma+=self.hijos[d-1].getValue()
        return suma
datos=[]
with open("input8.txt","r") as f:  
    fich=f.readline().strip().split()
    for d in fich:
        datos.append(int(d))

padre=Nodo(None,datos.pop(0),datos.pop(0))

padre.addHijos(datos)

print(padre.getValue())