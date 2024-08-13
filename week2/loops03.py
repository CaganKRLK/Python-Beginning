print("Tek Sayı Yazdırma")
limit = int(input("Bir sayı girin:\n"))
number = 1
if limit < 0:
    limit *= -1
while number <= limit:
    print(number)
    number += 2
