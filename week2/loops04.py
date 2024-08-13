print("Fibonacci Serisi")
limit = int(input("Bir limit belirle:\n"))
a, b = 0, 1
for _ in range(20):
    print("-", end="")
print()
while a <= limit:
    print(a)
    a, b = b, a + b
