# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBJAVpqrzQDFAWr&categoryId=AWBJAVpqrzQDFAWr&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 3282. 0/1 Knapsack
if __name__ == '__main__':

    WEIGHT = 0
    VALUE = 1

    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())

        items = []
        for _ in range(n):
            items.append(tuple(map(int, input().split())))  # (부피, 가치)

        items.sort(key=lambda x: (x[0], -x[1]))  # 부피 작고 가격 높은 순으로 정렬

        result = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # result [물건개수][가방무게]

        vol = 0

        for 물건개수 in range(1, n + 1):
            for 가방무게 in range(1, k + 1):  # 무게가 v일 때 최적의 결과
                weight, val = items[물건개수 - 1]

                if weight <= 가방무게:
                    result[물건개수][가방무게] = max(val + result[물건개수 - 1][가방무게 - weight], result[물건개수 - 1][가방무게])

                else:
                    result[물건개수][가방무게] = result[물건개수 - 1][가방무게]


        print(f"#{tc+1} {result[-1][-1]}")