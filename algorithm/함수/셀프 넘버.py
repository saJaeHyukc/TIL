num_1 = [x for x in range(1, 10001)]
num_2 = []
for i in num_1:
    if i < 10:
        a = i * 2
        num_2.append(a)
    elif i < 100:
        b = str(i)
        c = int(b) + int(b[0]) + int(b[1])
        num_2.append(c)
    elif i < 1000:
        d = str(i)
        e = int(d) + int(d[0]) + int(d[1]) + int(d[2])
        num_2.append(e)  
    elif i < 10000:
        f = str(i)
        g = int(f) + int(f[0]) + int(f[1]) + int(f[2]) + int(f[3])
        num_2.append(g)
    else:
        h = str(i)
        j = int(h) + int(h[0]) + int(h[1]) + int(h[2]) + int(h[3]) + int(h[4])
        num_2.append(h)     
num_3 = sorted(set(num_1) - set(num_2)) 
print(*num_3, sep='\n')

# 다른 사람과 코드 비교 TIL 적기

# result = [x for x in range(1, 10001)]

# for i in range(1, 10001):
#     j = i + sum([int(x) for x in str(i)])
#     try:
#         result.remove(j)
        
#     except:
#         pass
    
# print(result)

# result = [i for i in range(1, 10001)]
# number = 0
# number_list = []
# new_list = []
# for i in result:
#     number_list.clear() #number_list라는 값을 항상 초기화
#     number_list = list(str(i)) #number_list에 차례대로 더해야 하니 분리시켜 문자열로 만든 다음 list에 넣는다
#     number_list = list(map(int, number_list)) #리스트로 되어버린 값을 int로 변환
#     number = i + sum(number_list) #각각의 값과 i 값을 더하여 number에 넣음
#     new_list.append(number) #new_list에 첨부
# self_number = set(result) - set(new_list) #차집합   
# self_number = list(self_number) #집합을 리스트로 변환
# self_number.sort() #리스트 정렬
# print(*self_number,sep="\n") #모든 숫자에 대해서 ,을 대신 \n을 붙임