print("Sınav Sonucunu Yorumlat")
result = float(input("Sınav sonucun kaç?\n"))
success = str
if 100 >= result >= 85:
    success = "Çok İyi"
elif 85 > result >= 70:
    success = "İyi"
elif 70 > result >= 50:
    success = "Orta"
elif 50 > result >= 25:
    success = "Kötü"
elif 25 > result >= 0:
    success = "Çok Kötü"

if 100 >= result >= 0:
    print(f"Sınavdan aldığınız sonuç {success}.")
else:
    print("Hatalı Giriş!")
