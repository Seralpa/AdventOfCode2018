def operate(operation,registers):
    if operation[0]==0:#addr
        registers[operation[3]]=registers[operation[1]]+registers[operation[2]]
    elif operation[0]==1:#addi
        registers[operation[3]]=operation[1]+operation[2]
    elif operation[0]==2:#mulr
        registers[operation[3]]=registers[operation[1]]*registers[operation[2]]
    elif operation[0]==3:#muli
        registers[operation[3]]=operation[1]*operation[2]
    elif operation[0]==4:#banr
        registers[operation[3]]=registers[operation[1]]&registers[operation[2]]
    elif operation[0]==5:#bani
        registers[operation[3]]=operation[1]&operation[2]
    elif operation[0]==6:#borr
        registers[operation[3]]=registers[operation[1]]|registers[operation[2]]
    elif operation[0]==7:#bori
        registers[operation[3]]=operation[1]|operation[2]
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
            