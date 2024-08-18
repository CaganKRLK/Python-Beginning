def age(year,birthday):
    return year - birthday
def license(age):
    if age >= 18:
        return True
    else:
        return False
print(f"Ehliyet alabilirlik:\n{license(age(2024,2008))}")