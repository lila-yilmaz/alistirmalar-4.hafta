#Listenin içindeki çiftleri ve tekleri gruplama

liste= [1,2,3,4,5,6,7,8,9,10]
çift_liste=[]
tek_liste=[]
grupliste=[çift_liste, tek_liste]

for eleman in liste:
    if type(eleman) == int:
        if eleman % 2 == 0:
            çift_liste.append(eleman)
        else:
            tek_liste.append(eleman)

print(grupliste)
        
