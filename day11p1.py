tam=300
serial=2568
grid=[]

for i in range(tam-1):
    grid.append([])
    for j in range(tam-1):
        power=(((j+1+10)*(i+1))+serial)*(j+1+10)
        power=(power%1000)//100
        grid[i].append(power-5)

maximo=0
index=(0,0)
for i in range(len(grid)-2):
    for j in range(len(grid)-2):
        sum=0
        for x in range(i,i+3):
            for y in range(j,j+3):
                sum+=grid[x][y]
        if sum>maximo:
            maximo=sum
            index=(i,j)
print(index)
