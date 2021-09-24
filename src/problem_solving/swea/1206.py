for j in range(1, 11):
    size = int(input())
    data = list(map(int, input().split()))
    res = 0

    for i in range(2, size-2):
        target = data[i]
        near = sorted(data[i-2: i+3], reverse=True)
        if target == near[0]:
            res += (near[0] - near[1])
    print(f"#{j} {res}")
