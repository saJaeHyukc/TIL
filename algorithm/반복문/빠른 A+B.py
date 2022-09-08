import sys # sys.stdin.readline() 쓸 때 꼭 import 해줘야한다/

number = int(sys.stdin.readline()) #sys.stdin.readline() 이것은 input()보다 더 빨리 쓸 수 있다!!
for n in range(number):
    a, b =map(int, sys.stdin.readline().split())
    print(a + b)
# 1. 문자열 받을 때
# sentence = sys.stdin.readline() sys.stdin.readline()은 return값이 문자열이다
# sys.stdin.readline()을 출력하면 문자열에 개행문자(\n)가 기본으로 추가된 것을 확인 가능하다
# 2. 한 개의 정수를 입력받을 때
# 그냥 받으면 문자열로 받아지기에 정수로 입력받으려고 하면 int로 형변환을 해줘야한다.
# 형변환을 해주면 개행문자는 사라지고 그 형태만 남는다
# 3. 여러 개의 정수를 입력받을 때
# map함수로 여러 정수를 받을 수 있다 여러개의 정수를 입력할 때도 input보다 빠르다
# 4. 문자열 N줄을 입력받아 리스트에 저장할 때
# 문자열을 N개 라고 지정되어있는 경우 for문을 사용해 문자열 N개를 리스트에 저장할 수 있다
# 여기서 strip()은 문자열 앞과 끝의 공백문자를 제거해주는 함수다.
# lstrip() : 인자로 받은 문자를 String의 왼쪽에서 제거
# rstrip() : 인자로 받은 문자를 String의 오른쪽에서 제거 