import sys
sys.stdin = open('input (21).txt')
def perm(word, swap):
    global cnt, result
    # 횟수 만큼 swap
    if cnt == swap:
        return word

    for i in range(len(word)):
        for j in range(len(word)):
            word[i], word[j] = word[j], word[i]
            cnt += 1
            if word[]




T = int(input())
for tc in range(1, T+1):
    word, swap = input().split()
    cnt = 0
    result = ''
    perm(word, swap)

