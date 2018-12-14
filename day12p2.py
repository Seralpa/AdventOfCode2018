import re
ini=re.compile(r"initial state: ([.#]+)")
rule=re.compile(r"([.#]+) => ([.#])")
minimo=-4
patrones={}
updates=[]
plantas=[]
with open("input12.txt","r") as f:
    lines=f.readlines()
    state=ini.match(lines.pop(0)).group(1)
    plantas=list("".join(('....',state,'....')))

    #state=list(state)
    
    lines.pop(0)
    for l in lines:
        regla=rule.match(l)
        patrones[regla.group(1)]=regla.group(2)
        #patrones.append(list(regla.group(1)),list(regla.group(2)))
print("".join(plantas))
it=1
while it<=500: 
    updates=[]
    for p in range(len(plantas)):
        if p>1 and p<len(plantas)-2:
            patron="".join((plantas[p-2],plantas[p-1],plantas[p],plantas[p+1],plantas[p+2]))
            #print("p="+str(p)+" patron="+patron+" resultado="+patrones[patron])
            if plantas[p]!=patrones[patron]:
                updates.append(p)
    for u in updates:
        if plantas[u]=='.':
            plantas[u]='#'
        else:
            plantas[u]='.'
    if plantas[2]=='#':
        plantas.insert(0,'.')
        minimo-=1
    if plantas[3]=='#':
        plantas.insert(0,'.')
        minimo-=1
    if plantas[len(plantas)-3]=='#':
        plantas.append('.')
    if plantas[len(plantas)-4]=='#':
        plantas.append('.')
    inicio=""
    for p in plantas:
        if p=='#':
            break
        else:
            inicio+=p
    if len(inicio)>4:
        for _ in range(len(inicio)-4):
            plantas.remove('.')
        minimo+=len(inicio)-4
    suma=0
    for p in range(len(plantas)):
        if plantas[p]=='#':
            suma+=p+minimo
    print(suma)

    print(str(it)+"".join(plantas))
    it+=1

