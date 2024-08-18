def esiz_ogeleri_bul(liste):
  matchLess = []
  for number in liste:
    if number not in matchLess:
      matchLess.append(number)
  return matchLess

sayilar = [1, 3, 5, 3, 7, 9, 1, 5]
print("Eşsiz öğeler:", esiz_ogeleri_bul(sayilar))