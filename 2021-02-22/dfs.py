# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선탐색 경로를 출력하시오. 시작 정점을 1로 하시오.

G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [2, 6], [4, 5, 7], []]
GA = [0, 0, 0, 0, 0, 0, 0, 0]
     [0, 0, 1, 1, 0, 0, 0]
     [0, 1, 0, 0, 1, 1, 0, 0]


]

'''
def push(item):
    s.append(item)

def pop():
    if len(s) != 0:
        return s.pop(-1)
'''

def dfs(v):
    visited = [False] * 10
    s = []
    s.append(v)
    visited[v] = True
    while s:
        v = s.pop(-1) # v: vertax 현재의 점들, w: 인접한 점들
        print(v) # 목표점인지 체크
        for i in range(7):
            if not visited[v]:
             visited[v] = True # 방문 안한 경우
        for w in G[v]: # 인접한 거냐 아니냐만 체크할 수 있도록 손을 보는
            if not visited[w] and G[v][w] == 1:
                s.append(w)
                visited[w] = True


def dfsr(v): # recurssive 보기
    visited[v] = True
    print(v)
    # 목표치에 도달했어 하는 부분, print있는 부분이 나에겐 목표지점인 셈
    if v == '목표'
        return
    for w in G[v]:
        if not visited[w]:
            dfsr(w)
        dfsr(w)
    print(v)
    visited[v] = True

    for w in G[v]:
        if not visited[w]:
            dfsr(w)
            visited(w) = True


visited = [False] * 10








