def bmi_hesapla(kilo, boy):
    return kilo / (boy ** 2)

bmi = bmi_hesapla(70, 1.68)
print(f"BMI: {bmi:.1f}")
