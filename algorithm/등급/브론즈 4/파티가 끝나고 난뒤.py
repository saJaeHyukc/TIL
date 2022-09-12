L, P = map(int, input().split())
a = list(map(int, input().split()))
new_list = []
for i in range(5):
    b = a[i] - (L*P)
    new_list.append(b)
print(*new_list, sep=" ") 