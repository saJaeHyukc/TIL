new_list = []
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    new_list.append(a)
print(int(sum(new_list)/5))