t = int(input())

data = []
for _ in range(t):
    li = list(map(int, input().split()))

    sum = 0
    for i in li:
        if i % 2 == 0:
            continue
        else:
            sum += i
    data.append(sum)

for i in range(len(data)):
    print(f'#{i +1} {data[i]}')
