#parola

a=input("Lütfen sadece sayılardan oluşan 4 haneli bir parola oluşturunuz:")
parola = 0
if len(a) == 4 and a != str(a):
    parola += int(a)
    print("Parolanız:",parola)
else:
    print("Hatalı giriş!")


    
    
