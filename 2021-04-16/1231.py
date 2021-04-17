import sys
sys.stdin = open('')

class Node:
    left = None
    right = None
    num = 0
    val = ''

    def __init__(self, num):
        self.left = None
        self.right = None
        self.num = num
        self.val = ''


def printInOrder(root):
    tempStr = ""

    if root.left:
        tempStr += printInOrder(root.left)

    temp = root.val.replace('\n', '')
    tempStr += temp

    if root.right:
        tempStr += printInOrder(root.right)

    return tempStr


for i in range(0, 11):

    line = input()

    T = int(line)

    # 배열에다가 Node들을 쭉 저장
    nodeList = []

    for i in range(0, T):
        node = Node(i + 1)
        nodeList.append(node)

    for j in range(1, T + 1):

        temp = input()

        arr = temp.split(' ')

        if len(arr) > 2:  # 자식정보가 있는 줄
            '''
            print("노드번호: {0}".format(arr[0])  )
            print("노드 값: {0}".format(arr[1])  )
            print("자식노드 left: {0}".format(arr[2])  )

            if len(arr) > 3 :
                print("자식노드 right: {0}".format(arr[3])  )
            '''
            node = nodeList[int(arr[0]) - 1]
            node.val = arr[1]  # 값 세팅

            # 자식 노드 연결(왼쪽)
            node.left = nodeList[int(arr[2]) - 1]

            # 자식 노드 연결(오른쪽)
            if len(arr) > 3:
                node.right = nodeList[int(arr[3]) - 1]


        else:  # 자식정보가 없는 줄
            '''
            print("노드번호: {0}".format(arr[0])  )
            print("노드 값: {0}".format(arr[1])  )
            '''
            node = nodeList[int(arr[0]) - 1]
            node.val = arr[1]  # 값 세팅

    tempStr = printInOrder(nodeList[0])
    print('#%d %d' % (i, tempStr))
