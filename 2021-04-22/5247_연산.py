import sys
sys.stdin = open('sample_input (15).txt')

def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    check = {}
    while queue:
        item, cnt = queue.popleft()
        if check.get(item, 0): continue
        check[item] = 1
        if item == M: return cnt
        cnt += 1
        if 0 < item +1 <= 


cal = ['+1', '-1', '*2', '-10']
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#%d %d' %(tc, bfs(N, M)))
