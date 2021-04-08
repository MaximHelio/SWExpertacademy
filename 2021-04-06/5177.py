# import sys
# sys.stdin = open("sample_input.txt", "r")

class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self, num):
        if num >= 2:
            if self.lst[num] < self.lst[num // 2]:
                # 자리 바꾸기
                self.lst[num], self.lst[num // 2] = self.lst[num // 2], self.lst[num]
                self.sort(num // 2)  # 계속 정렬

    def append(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def my_sum(self, node):
        if node <= 1:
            return self.lst[node]
        else:
            return self.lst[node] + self.my_sum(node // 2)

    def my_result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2:
            return self.my_sum(last // 2)
        else:
            return 0


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    tree = Tree()
    for i in map(int, input().split()):
        tree.append(i)
    print('#%d %d' %(tc, tree.my_result()))


# lst = [....]
# HEAP = [0]
# for data in lst:
#     HEAP.append(data)
#     pos =
#     while 최상위가 아니면(까지) or 부모 노드의 값이 데이터 보다 작은 동안
#         부모 노드의 값과 현재 위치의 값을 변경한다.
#         현재 위치를 부모 노드의 위치로 변경(position= pos//2)
#
# while:
#     while 최상위가 아니면(까지) or 부모 노드의 값이 데이터 보다 적으면
#         현재 위치를 부모 노드의 위치로 변경(position= pos//2)
#         sumV += pos의 값


# import sys
# sys.stdin = open("sample_input.txt", "r")
