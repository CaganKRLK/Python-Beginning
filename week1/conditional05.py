
print("Seçim Yaş Hesaplama\nLütfen cevabınızı yıl olarak veriniz.")
birthday = int(input("Hangi yıl doğdun?\n"))
date = int(input("Hangi yıldasın?\n"))
election = int(input("Sonraki seçim hangi yıl?\n"))
age = date - birthday
electionUntil = election - date
x = age + electionUntil
if x >= 18:
    print("Yaşın seçime katılmak için yeterli.")
elif x < 18:
    print("Seçime katılmak içinbeklemen gerekicek.")
