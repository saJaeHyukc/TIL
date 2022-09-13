# import sys
# a, b, v = map(int , sys.stdin.readline().split())
# line = 0
# cnt = 0
# while True:
#     line += a 
#     if line >= v:
#         cnt += 1 
#         break
#     line -= b 
#     cnt += 1  
# print(cnt)

a,b,v = map(int, input().split())

if (v - b) % (a - b) == 0:
    print((v-b) // (a-b))
else:
    print((v-b) // (a-b)+1)

#못풀었던 키워드 정리
#시간초과가 되어서 x값이라는 것을 생각하여 종이에 식을 작성하자