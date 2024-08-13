print("Çarpım Tablosu")
number = int(input("Çarpım tablosunu görmek istediğiniz sayıyı yazın:\n"))
for _ in range(20):
    print("-", end="")
print()
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")
