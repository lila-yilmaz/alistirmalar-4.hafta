#Listenin içindeki sayıları toplayıp ekrana yazdırma

Sum=0
liste= [3, 4, 6, 7, 10, 1, 50]

liste.append(n)
for eleman in liste:
    if type(eleman) != str:
        Sum+=eleman
        

print("Liste içindeki sayıların toplamı",Sum,"dir.")
