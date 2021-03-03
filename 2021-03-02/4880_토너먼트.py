# 가위바위보
# 가위 1
# 바위 2
# 보 3
def win(x, y):
#       x      1, 2, 3
    win_x = [0, 3, 1, 2]  # x가 이기는 경우의 수
    if x != y:
        if win_x[x] == y:
            return x
    elif x == y:
        return x

    return y

# 토너먼트
def tournament(start, end):
    if start == end:
        return start
    round_1 = tournament(start, (start +end)//2)
    round_2 = tournament((start+end)//2+1, end)
    return win(round_1, round_2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    start = 1
    end = N
    print("#%d %d" %(tc, tournament(start, end)))
