import sys
sys.stdin = open("공통조상_input.txt")

def searchAnce(n):
    s = tree[n][2]
    p = []
    while s != 0:
        p.append(s)
        s = tree[s][2]
    return p

def findA(p1, p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]
    return 0  # 공통조상 없을 때

def preorder(node):
   global cnt
   if node != 0:
       cnt += 1  # root
       preorder(tree[node][0])  # 왼쪽
       preorder(tree[node][1])  # 오른쪽

T = int(input())
for tc in range(1, T+1):
    # 정점수, 간선수, 노드1, 노드2
    # 13 , 12 , 8번 13 번 공통 조상
    V, E, n1, n2 = map(int, input().split())
    tree = [[0] * 3 for _ in range(V+1)] #left, right, parent
    temp = list(map(int, input().split()))

    # 인접리스트로 입력 받기
    for i in range(E):# 0~11
        p = temp[i*2] #
        c = temp[i*2+1]
        if tree[p][0] == 0:  # 왼쪽자식이 없으면
            tree[p][0] = c      # 왼쪽자식에 저장
        else:
            tree[p][1] = c      # 오른쪽자식에 저장
        tree[c][2] = p      # 부모노드로 저장

    p1=[]
    p2=[]
    p1 = searchAnce(n1) # [2,1]
    p2 = searchAnce(n2) # [5, 2, 1]
    CA = findA(p1, p2) # 2
    cnt = 0
    preorder(CA) # 4
    print("#{} {} {}".format(tc, CA, cnt))