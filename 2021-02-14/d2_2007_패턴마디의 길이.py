import sys
sys.stdin = open("input (1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    inp = str(input())
    repeat = []
    for n in range(len(inp)):
        if inp[0:n] == inp[n:n+n]:
            repeat.append(n)
    print("#%d %d" %(tc, repeat[1]))






