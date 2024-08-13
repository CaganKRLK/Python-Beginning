print("Faktöryel Hesaplama")
number = int(input("Bir sayı girin:\n"))
total = 1
while number > 1:
    total *= number
    number -= 1
"""
for i in range(1, number + 1):
    total *= number
"""
"""
import math
total = math.factorial(number)
"""
print(f"Girdiğiniz sayının Faktöryeli:\n{total}")
