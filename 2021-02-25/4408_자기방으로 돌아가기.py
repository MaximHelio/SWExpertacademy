import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 돌아가야할 학생들의 수
    cor = [0] * 201
    for i in range(N):
        st, ed = map(int, input().split())
        if st > ed:
            st, ed = ed, st
        st = (st+1)//2
        ed = (ed+1)//2
        for j in range(st, ed+1):
            cor[j] += 1

    print("#%d %d" %(tc, max(cor))