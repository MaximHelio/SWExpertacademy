import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, 11):
    N, collection = input().split()
    stack = []
    for i in range(len(collection)):
        # stack이 비어있거나, stack의 마지막 값이 컬렉션 내 값과 일치하지 않는 경우
        # stack에 저장
        if not stack or stack[-1] != collection[i]:
            stack.append(collection[i])
        # stack에 값이 있고, stack의 마지막 값과 컬렉션 내 값이 같은 경우
        # stack에서 제거
        elif stack and stack[-1] == collection[i]:
            stack.pop()
    print("#%d" %(tc), end=' ')
    for i in stack:
        print(i, end ='')
    print()