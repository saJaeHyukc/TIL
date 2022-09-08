import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, input().split()))
print(min(a), max(a))
#최댓값 max() 최솟값 min()