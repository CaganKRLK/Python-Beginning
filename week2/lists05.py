print("Sıcaklık Dönüşümü")

print("İlk olarak vericeğiniz değerin cinsini seçin")
print("1. Celsius\n2. Fahrenheit\n3. Çıkış")
while True:
    kind = input("(1/2/3): ")
    if kind == "3":
        print("Çıkış yapılıyor ...")
        break
    value = float(input("Değer girin: "))
    if kind == "1":
        convertedV = (value*9/5)+32
        print(f"{value} Celsius = {convertedV} Fahrenheit")
    elif kind == "2":
        convertedV = (value-32)*5/9
        print(f"{value} Fahrenheit = {convertedV} Celsius")
    else:
        print("Hatalı Değer girdiniz!")
