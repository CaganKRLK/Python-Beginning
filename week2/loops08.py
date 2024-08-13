
print("Çift Sayıların Toplamı")
limit = int(input("Bir limit belirle: "))
total = 0
for i in range(limit):
    if i % 2 == 0:
        total += i
print(f"Toplam: {total}")

