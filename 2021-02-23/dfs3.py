import sys
sys.stdin = open("input (1).txt", "r")

def back(v):
    sw[v] = 1  # visited
    for i in gp[v]:
        if sw[i] == 1: continue
        else: back(i)

for _ in range(1, 11):
    gp = [] # 그래프
    sw = [] # visited -> 스위치로 표현
    for _ in range(99):
        gp.append([])
        sw.append(0)
    for _ in range(1, 11):
        tc, E = map(int, input().split()) # tc: 테스트 케이스 # E: 엣지 개수
        edges = input().split()

        for i in range(E):
            start, end = int(edges[i*2]), int(edges[i*2+1])
            gp[start].append(end)
        print(gp)
        back(0)
        print("#%d" %tc, end= " ")
        print(sw[99])