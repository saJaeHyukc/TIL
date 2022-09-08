n = int(input()) # 68
number = n
cnt = 0
while True:
    a = number // 10 # 6
    b = number % 10 # 8
    c = (a+b) % 10
    number = (10*b) + c
    cnt +=1
    if number == n:
        print(cnt)
        break
