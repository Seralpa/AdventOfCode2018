import re
import copy
before=re.compile(r"Before: \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)]")
operacion=re.compile(r"([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)")
after=re.compile(r"After:  \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)]")

def operate(operation,registers):
    if operation[0]==0:#addr
        registers[operation[3]]=registers[operation[1]]+registers[operation[2]]
    elif operation[0]==1:#addi
        registers[operation[3]]=registers[operation[1]]+operation[2]
    elif operation[0]==2:#mulr
        registers[operation[3]]=registers[operation[1]]*registers[operation[2]]
    elif operation[0]==3:#muli
        registers[operation[3]]=registers[operation[1]]*operation[2]
    elif operation[0]==4:#banr
        registers[operation[3]]=registers[operation[1]]&registers[operation[2]]
    elif operation[0]==5:#bani
        registers[operation[3]]=registers[operation[1]]&operation[2]
    elif operation[0]==6:#borr
        registers[operation[3]]=registers[operation[1]]|registers[operation[2]]
    elif operation[0]==7:#bori
        registers[operation[3]]=registers[operation[1]]|operation[2]
    elif operation[0]==8:#setr
        registers[operation[3]]=registers[operation[1]]
    elif operation[0]==9:#seti
        registers[operation[3]]=operation[1]
    elif operation[0]==10:#gtir
        if operation[1]>registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]==11:#gtri
        if registers[operation[1]]>operation[2]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]==12:#gtrr
        if registers[operation[1]]>registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]==13:#eqir
        if operation[1]==registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]==14:#eqri
        if registers[operation[1]]==operation[2]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]==15:#eqrr
        if registers[operation[1]]==registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0


antes=[]
despues=[]
operaciones=[]
with open("input16p1.txt") as f:
    for l in f:
        if before.match(l)!=None:
            matcher=before.match(l)
            antes.append([int(matcher.group(1)),int(matcher.group(2)),int(matcher.group(3)),int(matcher.group(4))])
        elif after.match(l)!=None:
            matcher=after.match(l)
            despues.append([int(matcher.group(1)),int(matcher.group(2)),int(matcher.group(3)),int(matcher.group(4))])
        elif operacion.match(l)!=None:
            matcher=operacion.match(l)
            operaciones.append([int(matcher.group(1)),int(matcher.group(2)),int(matcher.group(3)),int(matcher.group(4))])
cont=0
for o in range(len(operaciones)):
    coincidencias=0
    for i in range(16):
        operacion_ind=copy.deepcopy(operaciones[o])
        antes_ind=copy.deepcopy(antes[o])
        operate([i,operacion_ind[1],operacion_ind[2],operacion_ind[3]],antes_ind)
        if antes_ind==despues[o]:
            coincidencias+=1
    if coincidencias>=3:
        cont+=1
    
print(cont)