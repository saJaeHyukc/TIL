n = int(input()) 
for _ in range(n): 
    cnt, word = input().split() 
    for j in word:  
        print(j * int(cnt), end='')
    print()
        
