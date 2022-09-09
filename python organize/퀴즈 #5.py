# # continue, break
# absent = [2,5] #결석
# no_book = [7] #책을 깜빡했음
# for student in range(1, 11): 
#     if student in absent:
#         continue #스킵 하는 것!!! 이럴 때 쓰는 것이 continue의 역할 #다음 반복을 진행
#     elif student in no_book:
#         print(f"오늘 수업 여기까지.{student}는 교무실로 따라와")
#         break #반복문을 끝낼때!!!! #반복문을 끝냄
#     print(f"{student},책을 읽어봐")

# 한줄 for문
# 출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 ->101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students) #[101,102,103,104,105]
# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students) #[8,4,10[]
# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# 퀴즈
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *
cnt = 0
for i in range(1, 51):
    time = randint(5, 50)
    if 4 < time < 16: #범위 설정하는 것을 기억 못하냐.....
        print(f"[0]{i}번째 손님 (소요시간 : {time}분)")
        cnt += 1
    else:
        print(f"[ ]{i}번째 손님 (소요시간 : {time}분) ")

print(f"총 탑승 승객: {cnt}분")