import math
lim=math.sqrt(10551358)
suma=0
for i in range(1,int(lim)):
    if 10551358%i==0:
        suma+=i
        suma+=10551358/i
print(suma)