while True:
    a, b=map(int, input().split())
    if a > b:
        print("Yes")
    elif a==b==0:
        break
    elif a <= b:
        print("No")