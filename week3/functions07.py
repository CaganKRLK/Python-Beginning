numbers = [3, -5, 7, -2, 8, -1]
def detect(liste):
    positives = []
    negatives = []
    for number in liste:
      if number > 0:
        positives.append(number)
      elif number < 0:
        negatives.append(number)
    return positives, negatives

positives, negatives = detect(numbers)
print("Pozitif sayılar:", positives)
print("Negatif sayılar:", negatives)