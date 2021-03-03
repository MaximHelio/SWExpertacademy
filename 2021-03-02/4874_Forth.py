import sys
sys.stdin = open("sample_input.txt", "r")

###########후위 표기법의 수식을 이항연산을 이용해 연산##########
def pos_to_mid(inp):
    stack = []
    for i in range(len(inp)-1):
        if inp[i].isdigit():
            stack.append(inp[i])
        else:
            try:
                if inp[i] == "+":
                    stack[-2] == int(stack[-1]) + int(stack[-2])
                    stack.pop()
                elif inp[i] == "*":
                    stack[-2] == int(stack[-1]) * int(stack[-2])
                    stack.pop()
                elif inp[i] == "-":
                    stack[-2] == int(stack[-1]) - int(stack[-2])
                    stack.pop()
                elif inp[i] == "/":
                    stack[-2] == int(stack[-1]) / int(stack[-2])
                    stack.pop()
                result = stack[0]

            except: result = "error"
    if len(stack) != 1: result = "error"

    return result
T = int(input())
for tc in range(1, T+1):
    inp = list(map(str, input().split()))

    print("#%d %s" %(tc, pos_to_mid(inp)))