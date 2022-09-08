while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
#예외처리문으로 이렇게 할 줄은 상상도 못했다.