n = input()
alph = "abcdefghijklmnopqrstuvwxyz"
for i in alph:
    if i in n: #in은 i가 에 있는지 true, false로 판단하는 것 
        print(n.index(i), end=" ")
    else:
        print(-1, end=" ")
        
# S = input()
# check = [-1]*26 #[-1, -1, -1, .... 26개 있다는 뜻]
 
# for i in range(len(S)):
#     if check[ord(S[i])-97] != -1: # 해당 알파벳 중 중복이 있으면 여기로 
#         continue
#     else:
#         check[ord(S[i])-97] = i # 처음에는 else로 빠져서 -1 중 아스키코드를 숫자로 만들어 그 숫자만큼 빼주고 해당자리에 넣음
        
# for i in range(26):
#     print(check[i], end=' ')