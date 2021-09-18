n = int (input()) #n은 항상 10의 배수

coins = (500,100,50,10)

cnt = 0 #거슬러줘야할 동전의 최소 개수
for coin in coins:
    cnt += n//coin
    n %= coin
print(cnt)