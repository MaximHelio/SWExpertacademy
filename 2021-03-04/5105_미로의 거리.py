import sys
sys.stdin = open("sample_input (1).txt", "r")


def bfs(Q):
    global cnt
    while len(Q):
        new_Q = []
        # 큐가 빌때까지 반복
        while len(Q):
            start_i, start_j = Q.pop()
            for di, dj in dir:
                i = start_i + di
                j = start_j + dj
                if 0 <= i < N and 0 <= j < N:
                    if map_lst[i][j] == 0:
                        map_lst[i][j] = 1
                        new_Q.append((i, j))
                    if map_lst[i][j] == 3:
                        return cnt
        cnt += 1
        Q = new_Q
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_lst = [list(map(int, list(input()))) for _ in range(N)]
    cnt = 0
    Q= []
    #       상       하       좌       우
    dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(N):
            if map_lst[i][j] == 2:
                Q.append((i, j))
                break
        # 못찾았다면 위로 올린다.
        continue
        break
    print("#%d %d" %(tc, bfs(Q)))



#############################교수님 풀이#########################
재귀는 기반이 stack, 너비우선은 재귀로 안 만듦
dr = []
dc = []
def bfs(row, col):
    Q = []
    visited = [[False] * N for _ in range(N)]
    Q.append((row, col, 0))
    visited[row][col] = True
    while Q:
        row, col, cnt = Q.pop(0)
        #for dir in range(4):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR = row + dr
            newC = col + dc

            if 0 <= newR < N and 0 <= newC < N  and arr[newR][newC] !=1 and not visited[newR][newC]:
            #범위, 갈 수 있는 길인지 확인, visited, 안 간 길만 가도록
                if arr[newR][newC] == 3:
                    return cnt

                Q.append((newR, newC, cnt+1))
                visited[newR][newC] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input()] for _ in range(N)]
    for i in range(16):
        if 2 in arr[i]:
            row = i
            col = arr[i].index(2)
            break
    print(row, col, bfs(row, col))

# def bfs(start_i, start_j):
#     global cnt
#     Q.append((start_i, start_j))
#     visited.append((start_i, start_j))
#     while Q:
#         start_i, start_j = Q.pop(0)
#         new_i = []
#         new_j = []
#         for k in range(4):
#             new_i.append(start_i + di[k])
#             new_j.append(start_j + dj[k])
#             if any(new_i) and any(new_j) and (new_i, new_j) not in visited:
#                 Q.append((new_i, new_j))
#                 visited.append((new_i, new_j))
#                 for l in range(len(new_i)):
#                     for m in range(len(new_j)):
#                         dist[new_i[l]][new_j[m]] = dist[start_i][start_j] + 1
#                         if arr[new_i[l]][new_j[m]] == 3:
#                             cnt = dist[new_i[l]][new_j[m]] - 1
#                             return
#     return cnt
#
# T = int(input())
# #상, 하, 좌, 우
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2: start_i, start_j = i, j
#             if arr[i][j] == 3: end = [i, j]
#     cnt = 0
#     Q = []
#     dist = [[0] * N for _ in range(N)]
#     print("#%d %d" %(tc, bfs(start_i, start_j)))
#
