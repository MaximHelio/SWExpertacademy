import sys
sys.stdin = open('input.txt')
# 부분집합으로 생각

def dfs(L, sum, tsum): # 바둑이의 무게에 접근하는 인덱스
    global result 
    if sum + (total-tsum) < result:
        return
    if sum > c:
        return
    if L == n: # 종착점. 부분집합 하나가 완성
        if sum > result:
            result = sum
    else:
        dfs(L+1, sum+a[L], tsum+a[L])
        dfs(L+1, sum, tsum+a[L]) # a[L]번째 원소를 a의 부분집합으로 참여시키지 않겠다

if __name__ == '__main__':
    c, n = map(int, input().split()) # 전체 무게제한, 바둑이의 마리수
    a = [0] * n
    result = -21470000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    dfs(0, 0, 0)
    print(result)
