n = list(input())
a = int(len(n))
new_list=[]
for i in range(a):
    if (n[i].isupper()) == True:
        new_list.append(n[i].lower())
        
    elif (n[i].isupper()) == False:
        new_list.append(n[i].upper())
print(*new_list, sep="")

#str = input()
#print(str.swapcase()) #대문자는 소문자로!! 소문자는 대문자로!!