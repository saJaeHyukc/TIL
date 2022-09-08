#1. 해당 숫자 1을 걸려면 2초 // 2를 걸려면 3초...
#2. 숫자마다 해당하는 알파벳을 연결 
#3. 시간이 얼마나 걸리는지?
#- 바로 그냥 알파벳마다 시간이 걸리는 것을 지정해두고
#4. 단어는 대문자!

Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
result = 0

for i in a :
    for j in Number:
        # print(i)
        # print(j)
# 만약에 입력받은 값이 Number에 있으면 index에서 3초를 더해준다.
        if i in j :
            result += Number.index(Number) + 3


print(result)