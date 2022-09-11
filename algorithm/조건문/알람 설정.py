h, m = map(int, input().split())

m -= 45

if m < 0: #음수일 경우
    m = 60 + m
    h -= 1
    if  h < 0: #0시일 때 23시로 만들어주기
        h = 24 + h
print(h, m)