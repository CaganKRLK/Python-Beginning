text = "Kedi çok sevimli bir hayvandır. Kedi mırlamayı sever. Kediler harikadır."
word = "Kedi"

def wordQuantity(text, word):
    return text.count(word)

print(f'Metinde {wordQuantity(text,word)} kez "Kedi" kelimesi geçiyor.')