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