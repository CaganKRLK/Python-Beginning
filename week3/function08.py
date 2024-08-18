def not_ortalamasi(notlar):
    return sum(notlar) / len(notlar)

notlar = [85, 90, 60]
print(f"Not ortalaması: {not_ortalamasi(notlar):.2f}")
