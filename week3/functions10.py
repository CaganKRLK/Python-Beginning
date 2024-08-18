numbers = [1, 3, 5, 3, 7, 9, 1, 5]

def unique(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

print(f"Listedeki tekrar etmeyen sayılar\n{unique(numbers)}")