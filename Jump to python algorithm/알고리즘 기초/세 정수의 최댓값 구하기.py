#세 정수를 입력 받아 최댓값 구하기
a, b, c = map(int, input().split())
MAX = a
if b > MAX: MAX = b
if c > MAX: MAX = c
print(f'최댓값은 {MAX}입니다')
#조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변겨오디는데 이러한 구조를 선택 구조입니다
