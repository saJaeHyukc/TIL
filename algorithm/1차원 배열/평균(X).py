n = int(input())  
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list :
    new_list.append(score/max_score *100)  # 새로운 점수 생성
test_avg = sum(new_list)/n
print(test_avg)
#sum 이라는 함수를 잘 활용하자
#list 내부로 for문을 돌릴 수 있다는 사실도 잊지말자