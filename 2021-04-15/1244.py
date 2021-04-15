import sys
sys.stdin = open('input (21).txt')


T = int(input())
for tc in range(1, T+1):
    pos, swap = input().split()
    l = len(pos)
    perm(l, swap)
