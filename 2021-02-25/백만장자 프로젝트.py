import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 총 날짜의 수
    price_lst = list(map(int, input().split())) # 가격

    cnt = 0 #  price가 필요한 날짜
    purchase = 0 # 구매할 가격
    price = price_lst[-1]
    ans = 0
    for daily_price in price_lst[-2::-1]:
       if daily_price < price:
           cnt += 1
           purchase += daily_price
       elif daily_price >= price:
           ans += price * cnt - purchase
           price = daily_price
           cnt = 0; purchase = 0

    if cnt >= 1:
        ans += price * cnt - purchase

    print("#%d %d" %(tc, ans))

