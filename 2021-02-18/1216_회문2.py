import sys
sys.stdin = open("input (2).txt", "r")

T = 10
M_list = [i for i in range(1, 101)]
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(100):
        arr.append(input())
    # rough_arr = [list(input().split()) for _ in range(100)]

    ans = 0
    for M in M_list:
        for i in range(100): # 세로줄
            for j in range(100): # 가로줄 순회
                dis = int(M/2)
                if j - dis < 0: continue
                if j + dis >= 100: continue
                if arr[i][j-dis:j] == arr[i][j:j+dis]:
                    if M > ans: ans = M

    for M in M_list:
        for i in range(100): # 세로줄
            for j in range(100): # 가로줄 순회
                dis = int(M/2)
                if j - dis < 0: continue
                if j + dis >= 100: continue
                before = ''
                after = ''
                for k in range(dis~):
                    before +=
                for k in range(dis~):
                    before +=

                if before == after:
                    if M > ans: ans = M
    '''
    ans_M = []
    for M in M_list: # M = 반복되는 구간의 수 = 1부터 100까지
        # 가로
        for i in range(100):
            for j in range(100 - M + 1):
                s_lst = []
                for k in range(M):
                    s_lst.append(arr[i][j + k])
                if s_lst == list(reversed(s_lst)):
                    ans_M.append(M)
        # 세로
        for j in range(100):
            for i in range(100 - M + 1):
                s_lst = []
                for k in range(M):
                    s_lst.append(arr[i + k][j])
                if s_lst == list(reversed(s_lst)):
                    ans_M.append(M)
    '''
    print("#%d %s" % (tc, max(ans_M)))

def my_find2(M):
    for i in range(N):
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            tmp2 = zwords[i][j:j+M]
            if tmp == tmp[::-1] or tmp2 == tmp[::-1]:
                return M
    return 0


def my_find(M):
    #전체 크기가 N이다.
    for i in range(N):
        # 부분 문자열의 시작점
        for j in range(N-M+1):
            # 스왑을 응용한 회문검사
            # 가로 검사
            for k in range(M//2):
                # 앞뒤검사
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                # 회문이다.
                elif k == M//2 - 1:
                    return M
            # 세로 검사
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2 -1:
                    return M
    return 0

# 거꾸로 회문 검사 시행
for tc in range(10):
    tc_num = int(input())

    N = 100
    words = [input() for i in range(N)]
    zwords = list(zip(*words)) # 열을 가로로 바꾸는 방법
    #가장 길이가 긴 회문검사를 한다.
    for i in range(N, 0, -1):
        ans = my_find(i)

        if ans != 0:
            break

    print("#{} {}".format(tc_num, ans))