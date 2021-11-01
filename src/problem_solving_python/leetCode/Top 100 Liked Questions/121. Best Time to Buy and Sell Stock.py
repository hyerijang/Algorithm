from typing import List


# ! 실패 (18분) 시간초과
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit


# [모범답안]
# - inf를 float('inf')로 쓸수도 있구낭
def maxProfit(prices: List[int]) -> int:
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)  # 현재까지 본 가격중 가장 저렴한 가격
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


maxProfit([7, 1, 5, 3, 6, 4])
