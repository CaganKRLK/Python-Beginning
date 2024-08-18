def kelime_sayisi(metin, kelime):
    return metin.count(kelime)

metin = "Kedi çok sevimli bir hayvandır. Kedi mırlamayı sever. Kediler harikadır."
kelime = "Kedi"
print(f'"{kelime}" kelimesi {kelime_sayisi(metin, kelime)} kez geçiyor.')
