#1. 숫자 3개가 있으면 거꾸로 적힌다.ex) 327 -> 723 398 -> 893 숫자를 먼저 거꾸로 쓰는 함수 찾기
#2. 숫자 비교하는 것 ->조건문
#3. 같이 않는 세자리 수에 , 0이 포함되어 있지않다. 

a, b = map(int, input().split())
c = (a // 100) + (((a % 100) // 10) * 10) + ((a % 10)* 100) # 첫자리는 일의 자리 //두번 째 자리는 십의 자리 //세번 째 자리는 백의 자리
d = (b // 100) + (((b % 100) // 10) * 10) + ((b % 10)* 100)
if c > d:
    print(c)
else:
    print(d)

# a = int(str(a)[::-1]) #뒤집어 주는 것
# b = int(str(b)[::-1])
# if a > b:
#     print(a)
# else:
#     print(b)