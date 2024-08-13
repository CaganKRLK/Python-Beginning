nots = [70,85,90]
average = sum(nots)/len(nots)
if 100 >= average >= 85:
    success = "Çok İyi"
elif 85 > average >= 70:
    success = "İyi"
elif 70 > average >= 50:
    success = "Orta"
elif 50 > average >= 25:
    success = "Kötü"
elif 25 > avearge >= 0:
    success = "Çok Kötü"

if 100 >= average >= 0:
    print(f"Sınavlardan aldığınız sonuç {success}.\nOrralamanız: {average}")
else:
    print("Hatalı Giriş!")
