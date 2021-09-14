n = int(input())

data = [[0]*20  for _ in range(19)]

for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)

    data[a-1][b-1] = 1

for i in range(19): 
    for j in range(19):
        print(data[i][j],end=' ')
    print('')

