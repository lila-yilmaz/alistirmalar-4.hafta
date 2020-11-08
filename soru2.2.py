#Demetin içinde olan elemanlardan sadece str olanları yazdırma

demet= (2,3,4,2,14,"Mustafa",132,"Kemal","Atatürk",5)

for eleman in demet:
    if type(eleman) == str:
        print(eleman)
