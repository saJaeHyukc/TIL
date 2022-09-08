# class Student(): #인스턴스화 메서드란 객체의 새 인스턴스를 만들 때 마다 실행되는 메서드 // 기술적으로 괄호는 필요없다
    
#     planet = "Earth" #클래스 객체 속성 -> 모든 인스턴스에 대해 동일하다 //
#     #모든 인스턴스를 통틀어 동일한 값을 지니는 변수를 클래스 객체 속성이라 설명하는데, 클래스 정적 변수와 그 개념이 동일
    
#객체 지향 프로그래밍을 사용하면 반복 가능한, 조직적인 코드를 만들 수 있다
#관례적으로 클래스는 스네이크 케이스 대신 캐멀 케이스를 쓴다(낙타 표기법은 단어의 첫문자를 대문자로 표기한다)
#클래스 안에서 함수라고 하지 않고 대신, 그것들을 클래스 메서드 또는 클래스의 액트라고 한다. 일반적으로 클래스 내의 맴버 함수를 메서드라고 한다. 
#     def __init__(self, name, gpa): #인스턴스화 메서드 init 호출
        
#         self.name = name #그냥 객체
#         self.gpa = gpa

# stu1 = Student(name = "재혁", gpa = 4.0) 
# stu2 = Student(name = "기훈", gpa = 3.5) 
# print(stu1.planet)
# #클래스 호출의 일부분으로 속성을 가지고 있다면 , . 과 속성 이름을 사용할 수 있다는 것을 알 수 있음
# #객체의 인스턴스를 출력하면 컴퓨터의 메모리에 있는 이 지점에서 student 객체입니다 라고 알려줌

class Agent():
    
    origin = "USA" # 클래스 객체 속성 업데이트는 불가능하다는 것을 유념하자
    
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

x = Agent('Jose',6,170)
print(x.weight)
x.weight = 160  # 확실히 속성을 취해서 반환할 수 있고, 속성을 업데이트 할 수 있다는 것을 알 수 있음
print(x.weight)