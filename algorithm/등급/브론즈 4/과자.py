a = list(map(int, input().split()))
b = (a[0] * a[1]) - a[2]
if b > 0:
    print(b)
elif b <= 0:
    print(0)
