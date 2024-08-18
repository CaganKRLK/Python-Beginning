def bmiCalculate(
    choice = 0,
    weight = None,
    length = None,
    bmi = None,
    value = None
):
    if choice == 0:
        return (weight/(length**2))
    elif choice == 1:
        return bmi*(value**2)
    elif choice == 2:
        return (value/bmi)**(1/2)

print(f"{bmiCalculate(length = 1.87,weight = 96):.2f}")
# print(bmiCalculate(1,value = 1.87,bmi = 27))
# print(bmiCalculate(2,value = 96,bmi = 27))