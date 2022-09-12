while True:
    a = list(input())
    if a[0]=="E" and a[1]=="N" and a[2]=="D":
        break
    else:
        a.reverse()
        print(*a, sep="")