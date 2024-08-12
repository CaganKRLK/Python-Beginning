print("Giysi Öneri Sistemi")
heat = int(input("Bu gün hava kaç derece?\n"))
a = "giyebilirsiniz."
if heat >= 50:
    print("Çıkma!")
elif 50 > heat >= 20:
    print("İnce tişört ve şort",a)
elif 20 > heat >= 10:
    print("İnce ceket",a)
elif 10 > heat >= -10:
    print("Palto ve atkı",a)
elif -10 > heat:
    print("Çıkma!!")
else:
    print("Hatalı giriş yaptınız.")
