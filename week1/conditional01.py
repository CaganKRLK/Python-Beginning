print("***Hesap Makinesi***")
choice = int(input("İlk olarak yapmak istediğiniz işlemi seçin\n1: Toplama\n2: Çıkarma\n3: Çarpma\n4: Bölme\n"))
number1 = float(input("İlk sayıyı seçin:\n"))
number2 = float(input("İkinci sayıyı seçin\n"))
result = float
if choice == 1:
    result = number1 + number2
elif choice == 2:
    result = number1 - number2
elif choice == 3:
    result = number1 * number2
elif choice == 4:
    result = number1 / number2

print("İşleminin sonucu:", result)
