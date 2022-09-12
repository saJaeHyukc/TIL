a, b=map(int, input().split())
c = int(a - (a * (b / 100)))
if c < 100:
    print(1)
elif c >= 100:
    print(0)