exercise_plan = {
    "Pazartesi": 30,
    "Salı": 45,
    "Çarşamba": 20,
    "Perşembe": 35,
    "Cuma": 40,
    "Cumartesi": 50,
    "Pazar": 60
}

print("Egzersiz Planı Yönetimi")
print("1. Egzersiz planını görüntüle")
print("2. Egzersiz süresini değiştir")
print("3. Tüm günlerin egzersiz süresini değiştir")
print("4. Çıkış")

while True:
    choice = input("Seçiminizi yapın (1/2/3/4): ")

    if choice == "1":
        print("\nEgzersiz Planı:")
        for day, minutes in exercise_plan.items():
            print(f"{day}: {minutes} dakika")
        print()
    elif choice == "2":
        day = input("Gün girin (Pazartesi, Salı, ...): ")
        if day in exercise_plan:
            new_minutes = int(input(f"{day} için yeni egzersiz süresini dakika cinsinden girin: "))
            exercise_plan[day] = new_minutes
            print(f"{day} için egzersiz süresi {new_minutes} dakika olarak güncellendi.\n")
        else:
            print("Geçersiz gün adı. Lütfen geçerli bir gün girin.\n")
    elif choice == "3":
        print("\nGünlerin egzersiz sürelerini güncelleyin:")
        for day in exercise_plan:
            new_minutes = int(input(f"{day} için yeni egzersiz süresini dakika cinsinden girin: "))
            exercise_plan[day] = new_minutes
            print(f"{day} için egzersiz süresi {new_minutes} dakika olarak güncellendi.")
        print()
    elif choice == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçenek. Lütfen 1, 2, 3 veya 4 girin.\n")
