numbers = [12, -7, 9, -5, -12, 0, 34, -23, 18]
pozitive = 0
negative = 0
notr = 0
for i in numbers:
    if i > 0:
        pozitive += 1
    elif i < 0:
        negative += 1
    else:
        notr += 1
print(f"Listede:\n{pozitive} Pozitif\n{negative} Negatif\n{notr} Nötr\nSayı var.")

