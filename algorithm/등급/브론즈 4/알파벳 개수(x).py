n = int(input())
m = list(map(int, input().split()))
cnt = 0
for i in range(len(m)):
    if n == m[i]:
        cnt +=1
print(cnt)