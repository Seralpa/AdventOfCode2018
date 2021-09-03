
def operate(operation,registers):
    if operation[0]=='addr':#addr
        registers[operation[3]]=registers[operation[1]]+registers[operation[2]]
    elif operation[0]=='addi':#addi
        registers[operation[3]]=registers[operation[1]]+operation[2]
    elif operation[0]=='mulr':#mulr
        registers[operation[3]]=registers[operation[1]]*registers[operation[2]]
    elif operation[0]=='muli':#muli
        registers[operation[3]]=registers[operation[1]]*operation[2]
    elif operation[0]=='banr':#banr
        registers[operation[3]]=registers[operation[1]]&registers[operation[2]]
    elif operation[0]=='bani':#bani
        registers[operation[3]]=registers[operation[1]]&operation[2]
    elif operation[0]=='borr':#borr
        registers[operation[3]]=registers[operation[1]]|registers[operation[2]]
    elif operation[0]=='bori':#bori
        registers[operation[3]]=registers[operation[1]]|operation[2]
    elif operation[0]=='setr':#setr
        registers[operation[3]]=registers[operation[1]]
    elif operation[0]=='seti':#seti
        registers[operation[3]]=operation[1]
    elif operation[0]=='gtir':#gtir
        if operation[1]>registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]=='gtri':#gtri
        if registers[operation[1]]>operation[2]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]=='gtrr':#gtrr
        if registers[operation[1]]>registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]=='eqir':#eqir
        if operation[1]==registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]=='eqri':#eqri
        if registers[operation[1]]==operation[2]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0
    elif operation[0]=='eqrr':#eqrr
        if registers[operation[1]]==registers[operation[2]]:
            registers[operation[3]]=1
        else:
            registers[operation[3]]=0

ip=0
instr=[]
with open("input21.txt") as f:
    ip=int(f.readline()[4])
    instr=[l.strip().split() for l in f.readlines()]
for i in instr:
    for j in range(1,len(i)):
        i[j]=int(i[j])

fich=open("salida.txt","w")

registers=[0,0,0,0,0,0]
while registers[ip]<len(instr) and registers[ip]>=0:
    operate(instr[registers[ip]],registers)
    registers[ip]+=1
    if registers[ip]==29:
        fich.write("despues "+str(registers)+"\n")
print(registers)