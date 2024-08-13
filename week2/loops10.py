scores = [75, 82, 90, 66, 58]

total = 0
length = 0
for i in scores:
    total += i
    length += 1
average = total/length
result = "geçti" if average >= 50 else "kaldı"
print(f"Sınav sonuçlarınızın ortalaması: {average}\nBaşarı durumu: {result}")
