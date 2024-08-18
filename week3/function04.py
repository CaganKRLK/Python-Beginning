def cift_sayilari_bul(liste):
    ciftler = [] # ciftler = [sayi for sayi in liste if sayi % 2 == 0]
    for sayi in liste:
      if sayi % 2 == 0:
        ciftler.append(sayi)
    return ciftler

sayi_listesi = [1, 2, 3, 4, 5, 6, 7, 8]
print("Çift sayılar:", cift_sayilari_bul(sayi_listesi))