import sys
n, x = map(int, sys.stdin.readline().split())
a = list(map(int, input().split()))
for i in range(0, n):   
    if a[i] < x:
        print(int(a[i]))