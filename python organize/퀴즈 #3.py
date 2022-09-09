# 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower()) #전부 소문자
# print(python.upper()) #전부 대문자
# print(python[0].isupper()) #0번째의 값이 대문자이면 true 아니면 false
# print(len(python)) #문자의 길이 측정
# print(python.replace("Python", "Java")) #해당 문자를 찾아 변경하기
# index = python.index("n") #해당하는 문자가 몇번째 위치에 있는지 알려줌
# print(index)
# index = python.index("n", index + 1) # 두번 째 n을 찾게 되어 그 위치를 알려줌
# print(python.find("Java")) #해당하는 문자 위치 알려줌 또한 잘못된 값을 적으면 -1로 반환해준다. 
# print(python.index("Java")) #해당하는 문자의 잘못된 값을 적으면 에러가 뜬다 find와 차이 기억하기!!!
# print(python.count("n")) #해당하는 문자을 몇번 나오는지 알려줌 

# 탈출 문자
# \" \': 문장 내에서 따옴표
# 저는 "나도코딩"입니다
## print("저는 '나도코딩'입니다")
## print("저는 "나도코딩"입니다")
# print("저는 \"나도코딩\" 입니다.")
# print("저는 \'나도코딩'\입니다")

# \\ : 문장 내에서 \
# print("C:\\Users\\wogur\\AppData\\Local\\Programs\\Python\\Python310\\python.exe")

# \r :커서를 맨 앞으로 이동
# print("Red Apple\rPine") #PineApple

# \b :백스페이스(한 글자 삭제)
# print("Redd\bApple") #RedApple

# \t : 탭
# print("Red\tApple") #Red  Apple

# 퀴즈
#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#ex) http://naver.com
#규칙1: http:// 부분은 제외 => naver.com
#규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙3: 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!" 로 구성(!)
#ex) 생성된 비밀번호:nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
my_str = my_str[:my_str.index(".")]
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{url} 생성된 비밀번호:{pw}")