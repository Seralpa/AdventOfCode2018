import re
from collections import Counter
asleep=re.compile(r"\[([0-9]+-[0-9]+-[0-9]+) [0-9]+:([0-9]+)\] falls asleep")
wake=re.compile(r"\[([0-9]+-[0-9]+-[0-9]+) [0-9]+:([0-9]+)\] wakes up")
guard=re.compile(r"\[([0-9]+-[0-9]+-[0-9]+) ([0-9]+):([0-9]+)\] Guard #([0-9]+) begins shift")
class Guardia:
    def __init__(self,id):
        self.id=id
        self.suenos=[]
        self.despertar=[]
        self.turnos=[]

    def addTurno(self,fecha,minutos):
        self.turnos.append((fecha,minutos))

    def addDespertar(self,momentoDespertar):
        self.despertar.append(momentoDespertar)

    def addSueno(self,momentoSueno):
        self.suenos.append(momentoSueno)
    
    def getFechas(self):
        listaFechas=[]
        for t in self.turnos:
            listaFechas.append(t[0])
        return listaFechas

    def getTiempoGuardia(self,momento):
        for f in self.turnos:
            if f[0]==momento[0]:
                return momento[1]-f[1]
        
    def getMinutosDeSueno(self):
        listaMins=[]
        for s in self.suenos:
            mini=60
            iMin=0
            for d in range(len(self.despertar)):
                if s[1]==self.despertar[d][1]:
                    minsSuenoHoy=self.despertar[d][0]-s[0]
                    if minsSuenoHoy<mini and minsSuenoHoy>0:
                        mini=minsSuenoHoy
                        iMin=d
            listaMins.extend(range(s[0],self.despertar[iMin][0]))
        return listaMins
            

'''listaSueño=[(36,"1518-11-04"),(40,"1518-11-02"),(45,"1518-11-05")]
listaDespertar=[(50,"1518-11-02"),(46,"1518-11-04"),(55,"1518-11-05")]
g=Guardia(0)
for i in listaSueño:
    g.addSueño(i)
for i in listaDespertar:
    g.addDespertar(i)

print(g.getMinutosDeSueño())'''
    
listaGuardias=[]

with open("input4.txt","r") as f:
    listaLineas=f.readlines()

#listaLineas=["[1518-11-01 00:00] Guard #10 begins shift","[1518-11-01 00:05] falls asleep","[1518-11-01 00:25] wakes up","[1518-11-01 00:30] falls asleep","[1518-11-01 00:55] wakes up","[1518-11-01 23:58] Guard #99 begins shift","[1518-11-02 00:40] falls asleep","[1518-11-02 00:50] wakes up","[1518-11-03 00:05] Guard #10 begins shift","[1518-11-03 00:24] falls asleep","[1518-11-03 00:29] wakes up","[1518-11-04 00:02] Guard #99 begins shift","[1518-11-04 00:36] falls asleep","[1518-11-04 00:46] wakes up","[1518-11-05 00:03] Guard #99 begins shift","[1518-11-05 00:45] falls asleep","[1518-11-05 00:55] wakes up"]

for l in listaLineas:
    if guard.match(l) is not None:
        id=int(guard.match(l).group(4))
        minutos=int(guard.match(l).group(3))
        horas=int(guard.match(l).group(2))
        fecha=list(guard.match(l).group(1))
        dia=int(fecha[8]+fecha[9])
        mes=int(fecha[5]+fecha[6])
        if horas!=0:
            horas=0
            minutos=minutos-60
            if (dia==31):
                print("dia 31")
                print(dia)
                print(fecha)
                dia=1
                mes+=1
            elif mes in [2,4,6,9,11] and dia==30:
                print("dia 30")
                print(fecha)
                dia=1
                mes+=1
            else:
                dia+=1

            if mes<10:
                fecha[5]='0'
                fecha[6]=str(mes)
            else:
                fecha[5]=str(mes)[0]
                fecha[6]=str(mes)[1]
            if dia<10:
                fecha[8]='0'
                fecha[9]=str(dia)
            else:
                fecha[8]=str(dia)[0]
                fecha[9]=str(dia)[1]
        if not any([ g for g in listaGuardias if id==g.id ]):
            listaGuardias.append(Guardia(id))
        for g in listaGuardias:
            if g.id==id:
                g.addTurno(fecha,minutos)
            #if g.id==3449:
             #   print(g.turnos)
                
        
        #listaLineas.remove(l)
print("he acabado con los turnos")
for l in listaLineas:
    if asleep.match(l) is not None:
        fecha=list(asleep.match(l).group(1))
        hora=int(asleep.match(l).group(2))
        diffMin=120
        guardia=None
        for g in listaGuardias:
            '''print("\n\n\n")
            print(g.id)
            print(g.turnos)
            print(fecha)'''
            if fecha in g.getFechas():
                diff=g.getTiempoGuardia((fecha,hora))
                if diff<diffMin and diff>=0:
                    diffMin=diff
                    guardia=g
        guardia.addSueno((hora,fecha))
    elif wake.match(l) is not None:
        fecha=list(wake.match(l).group(1))
        hora=int(wake.match(l).group(2))
        diffMin=120
        guardia=None
        for g in listaGuardias:
            '''print("\n\n\n")
            print(g.id)
            print(g.turnos)
            print(fecha)'''
            if fecha in g.getFechas():
                diff=g.getTiempoGuardia((fecha,hora))
                if diff<diffMin and diff>=0:
                    diffMin=diff
                    guardia=g
        guardia.addDespertar((hora,fecha))       
            
max=0
masRepetido=-1
id=0
for g in listaGuardias:
    if len(g.getMinutosDeSueno())>0:    
        cnt=Counter(g.getMinutosDeSueno())
        if max<cnt.most_common(1)[0][1]:
            max=cnt.most_common(1)[0][1]
            masRepetido=cnt.most_common(1)[0][0]
            id=g.id
print(id)
print(masRepetido)