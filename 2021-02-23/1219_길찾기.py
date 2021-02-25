import sys
sys.stdin = open("input (1).txt", "r")

T = 10
for tc in range(1, T+1):
    tc, n = map(int, input().split())
    # 인접 리스트
    # {1:[3, 4], 2:[5, 9], 3:[7]}
    adj_list = list(map(int, input().split()))
    adj = {x:[] for x in range(100)}
    for i in range(0, n*2, 2):
        s = adj_list[i]
        e = adj_list[i+1]
        adj[s].append(e)
    print(adj)
    stack = [0]
    # 중복 탐색을 막기 위해 visit 활용
    visit = [0] * 100
    visit[0] = 1

    ans = 0
    while stack:
        c = stack.pop()
        for next in adj[c]:
            if next == 99:
                ans = 1
                break
            if visit[next] == 0:
                stack.append(next)
                visit[next] = 1
    print("#%d %d" %(tc, ans))