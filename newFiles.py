import os
def yeniDosyaOlustur(klasor,dosya,uzanti,sayi):
    if not os.path.exists(klasor):
        os.makedirs(klasor)
    
    for i in range(1,sayi+1):
        dosyaAdi = f"{dosya}{i:02d}.{uzanti}"
        dosyaPath = os.path.join(klasor,dosyaAdi)

        with open(dosyaPath, 'w') as f:
            pass
    print("Dosyalar oluşturuldu.")

klasor = input("Dosyaları Hangi klasörde oluşturmak istiyorsunuz: ")
dosya = input("Dosya adını girin: ")
uzanti = input("Dosya uzantısını girin: ")
sayi = int(input("Kaç adet dosya oluşturmak istiyorsunuz: "))

yeniDosyaOlustur(klasor,dosya,uzanti,sayi)
