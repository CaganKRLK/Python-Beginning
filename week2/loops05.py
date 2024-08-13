print("Asal mı?")
number = int(input("Bir sayı girin:\n"))
prime = True
for i in range(2, number - 1):
    if number % i == 0:
        prime = False
for _ in range(20):
    print("-", end="")
print()
if prime:
    print("Girdiğiniz sayı asal.")
else:
    print("Girdiğiniz sayı asal değil.")
