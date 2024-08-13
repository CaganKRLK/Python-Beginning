
print("Hesap Makinesi")
choice = int(input("İlk olarak yapmak istediğiniz işlemi seçin\n1: Toplama\n2: Çıkarma\n3: Çarpma\n4: Bölme\n"))
number1 = float(input("İlk Sayı: "))
number2 = float(input("İkinci Sayı: "))

if choice == 1:
    result = number1 + number2
elif choice == 2:
    result = number1 - number2
elif choice == 3:
    result = number1 * number2
elif choice == 4:
    result = number1 / number2
if not 1 <= choice <= 4:
    print("Hatalı Giriş!")
else:
    print(f"İşleminizin sonucu:\n{result}")
