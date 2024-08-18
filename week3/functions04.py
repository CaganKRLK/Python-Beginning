import math
numberList = [1,2,3,4,5,6,7,8]

def even(list):
    evenNumberList = []
    for i in list:
        if i % 2 == 0:
            evenNumberList.append(i)
    return evenNumberList
def odd(list):
    oddNumberList = []
    for i in list:
        if i % 2 == 1:
            oddNumberList.append(i)
    return oddNumberList
def factorial(list):
    factorialList = []
    for i in list:
        total = 1
        for x in range(1,i+1):
            total *= x
        factorialList.append(total)
    return factorialList


print(f"Listedeki çift sayıların faktöryelleri\n{factorial(even(numberList))}")
print(f"Listedeki tek sayıların faktöryelleri\n{factorial(odd(numberList))}")
