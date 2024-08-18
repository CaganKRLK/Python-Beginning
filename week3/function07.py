def sayilari_ayir(liste):
    pozitifler = []
    negatifler = []
    for sayi in liste
      if sayi > 0
        pozitifler.append(sayi)
      elif sayi < 0
        negatifler.append(sayi)
    return pozitifler, negatifler

sayilar = [3, -5, 7, -2, 8, -1]
pozitifler, negatifler = sayilari_ayir(sayilar)
print("Pozitif sayılar:", pozitifler)
print("Negatif sayılar:", negatifler)
