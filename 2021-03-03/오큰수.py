N = int(input())
number = list(map(int, input().split()))

stack = []
result = [-1 for _ in range(N)]

stack.append(0)
i = 1
while stack and i < N:
    while stack and number[stack[-1]] < number[i]:
        result[stack[-1]] = number[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in result:
    print(i, end=" ")