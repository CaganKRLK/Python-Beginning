print("Trafik Sistemi")
lightColor = str(input("Trafik lambasının rengi ne?\n").lower())
if lightColor == "kırmızı":
    print("Dur")
elif lightColor == "sarı":
    print("Bekle")
elif lightColor == "yeşil":
    print("Geç")
else:
    print("Hatalı giriş.")
