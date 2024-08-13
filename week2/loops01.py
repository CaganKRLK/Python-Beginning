print("Basamak Hesaplama")
number = int(input("Bir sayı girin:\n"))
digit = 0
if number == 0:
    digit += 1
elif number < 0:
    number *= -1
while number > 1:
    number /= 10
    digit += 1
print(f"Girdiğin sayı {digit} basamklı.")
