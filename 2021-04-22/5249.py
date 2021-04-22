import sys
sys.stdin = open('sample_input (14).txt')

def MST_prim(G):
    key = [float]



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
