#Şirket çalışanlarından sadece Çankaya'da yaşayanları ekrana bastırma

sözlük = {"Mustafa Bey":"Çankaya","Kerim Bey":"Etimesgut","Ezgi Hanım":"Çankaya","Oğuz Bey":"Yüzüncüyıl"}

for key, value in sözlük.items():
    if value == "Çankaya":
        print(key)
