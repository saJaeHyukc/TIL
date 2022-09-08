import sys
a = int(sys.stdin.readline())
for i in range(1, a+1):  
    print(" " * (a - i), end="") # 공백이 있다는 것을 알자 하나 씩 프로그래밍 사고적 방식로 접근!!!
    print('*' * i) # end라는 연산자는 뒤에 print와 개행없이 붙여주는 역할을 한다!!!