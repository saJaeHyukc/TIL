n = int(input())
hansu = 0
for i in range(1, n+1):
    a_list = list(map(int, str(i)))
    if i < 100: # 1 ~ 99는 비교할 대상이 없어 등차수열!
        hansu += 1
    elif a_list[0]- a_list[1] == a_list[1] - a_list[2]: # 100의 자릿수 부터 비교하여 더하기!
        hansu += 1
print(hansu)
