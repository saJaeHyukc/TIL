n = input().upper() #입력받은 값 전부 대문자로
n_list = list(set(n)) #n에서 중복된 값을 없애고 list형태로 바꾼다

cnt =[] #n_list의 요소들이 각각 몇개가 있는지 개수를 cnt에 추가

for i in range(len(n_list)): # 중복된 값의 리스트 범위만 적고
    print(n_list[i])
    cnt.append(list(n).count(n_list[i])) # cnt에 알파벳 갯수를 적는다
    print(cnt)   
    Max = max(cnt) # 가장 높은 숫자를 넣는다
    print(Max)
    
    # [b, a, c] [1, 3, 1]
    print(cnt)
if cnt.count(Max) != 1: #max가 
    print("?")
else:
    print(n_list[cnt.index(Max)])        
#upper과 count 함수