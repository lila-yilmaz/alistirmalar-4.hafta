#5 futbolcunun bilgilerini alarak Barcelona takımında oynayan futbolcuların
#listesini liste içinde ekrana bastırma

futbolcular=[]
barcelona=[]
n=0
while n <5:
    ad=input("Ad:")
    soyad=input("Soyad:")
    takım=input("Takımı:")
    futbolcular.append([ad,soyad,takım])
    n+=1
    
for bilgi in futbolcular:
    if bilgi[2] == "Barcelona":
        barcelona.append(bilgi)

print(barcelona)
    
