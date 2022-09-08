n = int(input())
for i in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == "O":
            score +=1
            sum_score += score
        else:
            score = 0
    print(sum_score)
#나는 for문 안에 있는 for문을 list에 넣을 생각을 왜 못했을까... 변수 지정하는 것도 아직 너무 서툴다



