# https://swexpertacademy.com/main/code/problem/problemSubmitHistory.do?contestProbId=AV5LrsUaDxcDFAXc
# 백만장자 프로젝트
# 실행시간 : 4,131 ms
# 더 줄일수 있을 것 같긴한데...
from collections import deque

if __name__ == '__main__':
    t = int(input())  # 테스트 케이스 수

    TODAY = 0

    for case in range(1, t + 1):
        n = int(input())  # N(2 ≤ N ≤ 1,000,000)
        prices = deque(map(int, input().split()))  # 길이 : n
        정답 = 0
        최고가갱신일 = 0

        while prices:
            #언제부터 사도 좋을지 탐색한다.
            # - 최고가보다 저렴할 때 사서, 최고가인 날에 파는게 이득
            while prices:
                최고가 = max(prices)
                최고가갱신일 = prices.index(최고가)

                if 최고가갱신일 != TODAY:  # => 오늘은 최고가 보다 싸므로 구매 시작
                    break

                prices.popleft()  # 오늘이 최고가임 = 사면 손해이므로 이 날은 구매하지 않는다 (구간에서 제거)

            # 오늘부터 계속 사서 최고가인 날에 판다.
            시세차익 = 0
            for day in range(TODAY, 최고가갱신일):
                현재가 = prices[day]
                시세차익 += (최고가 - 현재가)

            정답 += 시세차익

            # 오늘부터 최고가인 날까지는 사서 팔았으므로
            for _ in range(최고가갱신일):
                prices.popleft()  # 이 구간은 제거한다.

        print(f"#{case} {정답}")
