#Demetin içinde aynı olan elemanları teke indirip ekrana yazma

demet=(1,1,1,2,2,3,3,"Mustafa","Mustafa",3.14,3.14)
liste=[]

for eleman in demet:
    if not eleman in liste:
        liste.append(eleman)

print(liste)
