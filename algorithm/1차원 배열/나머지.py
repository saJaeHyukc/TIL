list = []
for i in range(10):
    a = int(input())
    b = a % 42
    list.append(b)
list = set(list)
print(len(list))
    
#append로 리스트의 값을 저장하고 set로 중복된 값을 없애주고 len으로 길이를 파악한다!
# 처음부터 set을 줘버리면 오류가 발생한다 왜그런 것일까 그러고 set을 쓰고 값을 저장해야함