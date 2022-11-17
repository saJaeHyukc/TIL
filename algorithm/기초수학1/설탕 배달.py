n = int(input())

if n % 5 == 0:
    print(n//5)
else:
    num = 0
    while n > 0:
        n -= 3
        num += 1
        if n % 5 == 0:
            num += n//5
            print(num)
            break
        elif n == 0:
            print(num)
            break
        elif n==1:
            print('-1')
            break