class Node:

    def __init__(self, num):
        self.left = None
        self.right = None
        self.num = num
        self.val = ''

# traverse tree post-order
def calc(root):
    if root:
        if root.left:
            a = int(calc(root.left))

        if root.right:
            b = int(calc(root.right))

        if root.val == '/':
            return int(a / b)
        elif root.val == '*':
            return int(a * b)
        elif root.val == '+':
            return int(a + b)
        elif root.val == '-':
            return int(a - b)
        else:
            return root.val


def main():
    f = open("input.txt", "r")

    for testNum in range(1, 11):

        line = f.readline()
        if not line:
            break

        T = int(line)

        nodeList = []

        for i in range(0, T):
            nodeList.append(Node(i + 1))

        for test_case in range(1, T + 1):

            temp = f.readline()
            arr = temp.split(' ')

            if len(arr) > 2:
                node = nodeList[int(arr[0]) - 1]
                node.val = arr[1]
                node.left = nodeList[int(arr[2]) - 1]
                node.right = nodeList[int(arr[3]) - 1]

            else:
                node = nodeList[int(arr[0]) - 1]
                node.val = arr[1]

        print("#{0} {1}".format(testNum, calc(nodeList[0])))

        testNum += 1


if __name__ == '__main__':
    main()