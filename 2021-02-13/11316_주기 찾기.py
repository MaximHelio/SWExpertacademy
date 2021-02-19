import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    s, p, q, m = map(int, input().split())
    A0 = s
    Ai = (pㆍAi - 1 + q) mod m(i≥1)
