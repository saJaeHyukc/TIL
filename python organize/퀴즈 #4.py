# 리스트[]
# subway = [10, 20, 30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# 조세호 씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
# 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# 정형돈씨를 유재석/조세호 사이에 태워봄
# subway.insert(1, "정형돈") #["유재석","정형돈","조세호", "박명수","하하"]
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #["유재석","정형돈","조세호", "박명수"]
# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) #2
# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# 순서 뒤집기 가능
# num_list.reverse()
# 모두 지우기
# num_list.clead()
# 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# 리스트 확장
# num_list.extend(mix_list)

# 사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet.get(3)) # 3이라는 값을 가져옴
# pront(cabinet[5]) #없는 값을 넣으면 에러 뜸
# print(cabinet.get(5)) #없는 값을 넣으면 None이라는 값뜸
# print(cabinet.get(5, "사용 가능"))
# print(3 in cabinet) #True
# print(5 in cabinet) #False
# 새 손님
# cabinet[4] = "조세호" #해당 값 추가
# cabinet[3] = "김종국" #해당 값이 없어지고 업데이트
# 간 손님
# del cabinet[3] #키를 삭제
# key들만 출력
# print(cabinet.keys())
# value들만 출력
# print(cabinet.values())
# key,value 쌍으로 출력
# print(cabinet.items())
# 목욕탕 폐점
# cabinet.clear #해당 값 초기화

# 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# menu.add("생선가스") #변경 불가!!!!!!!!!!!
# name = "김종국"
# age = 20
# hobby = "운동"
# (name, age, hobby) = ("김종국", 20, "운동") #
# print(name, age, hobby)

# 집합(set)
# 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set) #{1,2,3}
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# 교집합(java와python 을 모두 할 수 있는 개발자)
# print(java & python) #유재석
# print(java.inersection(python)) #유재석
# 합집합(java할 수 있거나 python을 할 수 있는 개발자)
# print(java | python) #{"유재석", "김태호", "양세형", "박명수"}
# ptin(java.union(python))
# 차집합
# print(java - python) {"김태호", "양세형"}
# print(java.difference(python))
# python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# java를 잊어버림
# java.remove("김태호")

# 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) #class = set
# menu = list(menu)
# print(menu, type(manu)) #class = list
# menu = tuple(menu)
# print(menu, type(manu)) #class = tuple

# 퀴즈
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다
# 추첨 프로그램을 작성하시오

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 -- 
# 치킨 당첨자: 1
# 커피 당첨자: [2,3,4]
# -- 축하합니다 -- 

#(활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
lst = list(range(1,21)) #1부터 20까지 숫자를 생성
shuffle(lst)
winners = sample(lst, 4) #4명 중에서 1명은 치킨 ,3명은 커피
print("-- 당첨자 발표 -- ")
print(f"치킨 당첨자:{winners[0]} ")
print(f"커피 당첨자: {winners[1:]} ")
print("-- 축하합니다 --  ")

