T = int(input())
for tc in range(1, T+1):
    num1, num2 = map(int, input().split())
    if num1 == num2: result = "="
    elif num1 > num2: result = ">"
    else: result = "<"
    print("#%d %s" %(tc, result))