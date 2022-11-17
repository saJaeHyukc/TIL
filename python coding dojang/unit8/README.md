# 불과 비교, 논리 연산자 알아보기

## 불과 비교 연산자 사용하기
- 객체가 같은지 비교하기

```python
1 == 1.0 # True
1 is 1.0 # False
1 is not 1.0 #True
```
같다는  == , 다르다는 !=이 이미 있는데 is, is not을 왜 만들었을까?<br>
== !=는 값 자체를 비교하고, is, is not은 객체(object)를 비교한다.<br>

### <span style='background-color: #ffdce0'>참고</span>
- 정수 객체와 실수 객체가 서로 다른지 어떻게 확인가능?
  
정수 객체와 실수 객체가 서로 다른 것은 어떻게 확인하냐면 id함수를 쓰면 된다<br> id는 객체의 고유한 값(메모리 주소)를 구한다. (이 값은 파이썬을 실행하는 동안에는 계속 유지되며 다시 실행하면 달라진다.)
```python
id(1) #1714767504
id(1.0) #55320032
```
두 객체의 고유한 값이 다르므로 서로 다른 객체이며 is로 비교하면 False가 나온다. <br> 위에서 말했던 것 처럼 is와 is not은 객체(object)를 비교한다.

- 값 비교에 is를 쓰지 않기

값 비교할 때는 is를 사용하면 안된다. 왜냐하면 변수 a가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라질 수 있기 때문이다.
```python
a = -5
a is -5
#True

a = -6
a is -6
#False
```
<hr>

## 논리 연산자 사용하기
### <span style='background-color: #ffdce0'>참고</span>
- 정수, 실수, 문자열을 불로 만들기

정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 된다.<br>
이때 정수 1은 True, 0은 False이고 문자열의 내용이 'False'이면 불은 True이다.<br> 문자열의 내용 자체는 판단하지 않으며 값이 있으면 True이다.<br> 즉 정수 0, 실수 0.0이외의 모든 숫자는 True이다. 그리고 빈 문자열 '', ""를 제외한 모든 문자열은 True이다.
```python
bool(1) #True
bool(0) #False
bool(1.5) #True
bool('False') #True
```

