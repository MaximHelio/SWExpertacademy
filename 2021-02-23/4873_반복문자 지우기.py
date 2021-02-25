import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
for tc in range(1, T+1):
    inp = list(input())
    for i in range(len(inp)-1):
        if inp[i] == inp[i+1]:
            inp.remove(inp[i])
