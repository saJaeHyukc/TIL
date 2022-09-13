n = int(input()) 
line = 1

while n > line: 
    n -= line 
    line += 1 

if line % 2 == 0: 
    up = n 
    down = line - n + 1 
else: 
    up = line - n + 1 
    down = n 

print(up,'/',down, sep="")

#못풀었던 키워드 정리
#규칙을 못찾음