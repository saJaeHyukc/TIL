n = 9
list = []
for i in range(n):
    b = int(input())
    list.append(b)

print(max(list), list.index(max(list)) + 1 )
# 그 리스트 값의 위치 list.index()
    