
class Rect:
    def __init__(self,distancias,tam,id):
        self.dist0=int(distancias[0])
        self.dist1=int(distancias[1])
        self.tam0=int(tam[0])
        self.tam1=int(tam[1])
        self.id=id

    def fillRect(self,matrix):
        for i in range(self.dist0,self.dist0+self.tam0):
            for j in range(self.dist1,self.dist1+self.tam1):
                if matrix[i][j]!=0:
                    matrix[i][j]="x"
                else:
                    matrix[i][j]=id

    def isFull(self,matrix):
        for i in range(self.dist0,self.dist0+self.tam0):
            for j in range(self.dist1,self.dist1+self.tam1):
                if matrix[i][j]=="x":
                    return False
        return True

matrix=[[0 for i in range(1000)] for j in range(1000)]
listaRects=[]
cont=0

with open("input3.txt","r") as f:
    for line in f:
        line=line.split()
        id=int(line[0].replace("#",""))
        distancias=line[2].replace(":","").split(",")
        tam=line[3].split("x")
        rect=Rect(distancias,tam,id)
        rect.fillRect(matrix)
        listaRects.append(rect)

for r in listaRects:
    if r.isFull(matrix):
        print(r.id)
