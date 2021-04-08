import sys
sys.stdin = open('input.txt', 'r')

# 무슨 순회인지 찾기
def order(node):
    # 노드의 범위를 벗어나지 않을 때만
    if node <= N:
        # value가 사칙연산 중 하나인 경우
        if type(tree[node]) is str:
            left_value = order(left[node])
            right_value = order(right[node])
            if tree[node] == "+":
                tree[node] = left_value + right_value
            elif tree[node] == "-":
                tree[node] = left_value - right_value
            elif tree[node] == "*":
                tree[node] = left_value * right_value
            elif tree[node] == "/":
                tree[node] = left_value / right_value
        return tree[node]

T = 10
for tc in range(1, T+1):
    N = int(input())
    #인덱스 맞추기
    tree = [0] * (N + 1)
    # 힙 아닐 수도 있으므로
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    lst = ['+', '-', '*', '/']
    for _ in range(N):
        idx, value, *arg = input().split()
        idx = int(idx)
        if value not in lst:
            value = int(value)
        tree[idx] = value
        if arg:
            left[idx] = int(arg[0])
            if len(arg) == 2:
                right[idx] = int(arg[1])
    result = order(1)
    print("#%d %d" %(tc, int(result)))
