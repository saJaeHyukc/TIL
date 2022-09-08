n = int(input())
for _ in range(n):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    cnt = 0
    for scores in score[1:]:
        if avg < score:
            cnt +=1
    rate = (cnt/scores[0]) * 100
    print('%.3f' %rate + '%')
#문제를 잘 읽어보자!!!
#한 입력값을 받은 다음 리스트 칸을 나눠 평균을 나눈다는게 신기했다
# 파이썬 소수점 자리 제한 방법은
# 1. round함수 사용 2. format서식으로 소수점 관리
# 3. 파이썬 f-string에서 소수점 관리 4. %.?f로 소주점 관리 