h, m = map(int, input().split())
t = int(input())

h += t // 60 
m += t % 60

if m >= 60: #60분이 넘어가면 시간을 더하고 60분을 뺀 분을 표시한다
    h += 1
    m -= 60
if h >= 24: #24시가 넘어가면 해당 시간 값을 빼준다
    h -= 24
    
print(h, m)