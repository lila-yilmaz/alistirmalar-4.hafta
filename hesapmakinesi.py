#hesap makinesi

while True:
    a=input("Bir sayı giriniz: ")
    işlem=input("İşlem giriniz: ")
    b=input("Bir sayı daha giriniz: ")
    if type(a) == int and type(b)== int and işlem == "+":
        print("=",a+b)
    elif type(a) == int and type(b)== int and işlem == "-":
        print("=",a-b)
    elif type(a) == int and type(b)== int and işlem == "x":
        print("=",a*b)
    elif type(a) == int and type(b)== int and işlem == "/":
        print("=",a/b)
    else:
        print("Hatalı girdi!")
    
    
