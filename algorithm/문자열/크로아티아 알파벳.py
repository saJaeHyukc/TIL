# # 크로아티아 알파벳 조건마다 빼주기
# # 갯수 세아리기
a = input()
sum = len(a)
for i in range(len(a)):
    if a[i:i+2] == "c=": #i이상 i+2미만
        sum -= 1
    elif a[i:i+2] == "c-":
        sum -= 1
    elif a[i:i+2] == "d-":
        sum -= 1
    elif a[i:i+2] == "lj":
        sum -= 1
    elif a[i:i+2] == "nj":
        sum -= 1
    elif a[i: i+2] == "s=":
        sum -= 1
    elif a[i: i+2] == "z=":
        sum -= 1
        if a[i-1:i] == "d":
            sum -= 1
print(sum)        
    
#croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
#s = input()
#for c in croatia:
#   s = s.replace(c, "*")
#print(len(s))