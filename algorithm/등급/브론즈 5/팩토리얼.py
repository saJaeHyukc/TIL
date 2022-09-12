n = int(input())
total = 1
for i in range(1, n+1):
    total *= i
    if n == 0:
        print(1)
print(total)