
import sys

def areSimilar(l1,l2):
    diff=0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            diff+=1
        if diff>1:
            break
    return diff==1

lineas=[]

with open("input2.txt","r") as f:
    lineas=f.readlines()

for line in lineas:
    lineas.remove(line)
    for parecida in lineas:
        if areSimilar(line,parecida):
            print(line)
            print(parecida)
            sys.exit()