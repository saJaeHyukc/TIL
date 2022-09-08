try:
    print(10 + 10) 
    # url을 방문하거나, 데이터베이스 명령을 수정하려고 시도하게 된다. 
    # 그런 다음 오류가 있으면 그에 대한 오류 메시지를 사용자에게 보고한다. 
    # 이럴 때는 html코드를 넣거나 다른페이지로 이동하거나 새로고침 같은 작업을 수행할 수 있다
except IOError:
    print("입 출력 에러")
    print("파일 허가를 확인했냐?")
except TypeError:
    print("너는 잘못된 타입을 쓰고 있다")
except:
    print("너는 에러를 가지고 있다!")
# else: #예외가 발생하지 않는 경우에만 실행된다
#     print("이상 없다!")
finally: # 예외가 있어도 없어도 코드는 실행한다. 오류 및 예외 처리 구문
    print("에러가 있던 없던 난 실행~")

# #퀴즈
# def divider(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         print("Please do not divide by zero!")

# try:
#     실행할 코드
# except 예외 as 변수:
    # 예외가 발생했을 때 처리하는 코드