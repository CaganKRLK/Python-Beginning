print("Çekim Hesabı")
balance = float(input("Hesabınızda ne kadar var?\n"))
price = float(input("Ne kadar para çekmek istiyorsun?\n"))
remainder = balance - price
if balance >= price:
    print(f"Para çekme işlemi gerçekleştirilebilir.\nİşlem sonucu kalıcak olan bakiye {remainder}tl olucaktır.")
elif balance < price:
    print(f"İşlem gerçekleştirilemez.\n{remainder*-1}tl eksiğin var.")
