new_list = []
for i in range(3):
    a = int(input())
    new_list.append(a)
if new_list[0]==new_list[1]==new_list[2] == 60:
    print("Equilateral")
elif sum(new_list)==180 and (new_list[0]==new_list[1] or new_list[0]==new_list[2] or new_list[1] == new_list[2]):
    print("Isosceles")
elif sum(new_list)==180 and (new_list[0]!=new_list[1]!=new_list[2]):
    print("Scalene")
elif sum(new_list)!=180:
    print("Error")