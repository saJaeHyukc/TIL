numbers = int(input())
fix= [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(fix)):   
    new_fix = list(map(int, fix))
    print(f'{numbers} * {new_fix[i]} = {numbers * new_fix[i]}')
    