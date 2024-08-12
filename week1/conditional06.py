print("İndirim Hesaplama")
price = float(input("Aldığın ürünler ne kadar tuttu?\n"))
discount = float(input("Ürünlere ne kadar indirim uygulanacak? (%)\n"))
discountValue = (price/100)*discount
if not 100 >= discount >= 0:
    print("Lütfen 0 ile 100 arasında bir sayı girin.")
else:
    print(f"Ürünlere {discountValue}tl indirim uygulandı.\nİndirim sonrası fiyat {price - discountValue}tl.\nİyi Alışverişler : )")

