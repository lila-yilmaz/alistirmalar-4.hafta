#String'in içindeki harflerin kaç defa geçtiğini bulup sözlüğe atama

string= input("String giriniz:")
sözlük={}

for harf in string:
    if harf in sözlük:
        sözlük[harf]+=1
    else:
        sözlük[harf]=1
    
print(sözlük)
    
