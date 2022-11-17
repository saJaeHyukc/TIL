t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    yy = 1			# 층수
    xx = 1			# 호수
    while n > h:
        n -= h
        xx += 1
    yy = n
    print(yy*100+xx)
    
#못풀었던 키워드
#변수 생각/while문 활용/규칙 생각
        
