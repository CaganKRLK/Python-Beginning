numbers = [23, 45, 12, 78, 56, 89, 34]
biggest = numbers[0]
index = 0
for i in numbers:
    index += 1
    if i > biggest:
        biggest = i
        indexBgst = index

print(f"Listede ki en en büyük sayı {biggest}.\nlistedeki sırası {indexBgst}.")
