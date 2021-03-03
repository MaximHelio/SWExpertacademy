import sys
sys.stdin = open("input.txt", "r")

def post_cal(result):
    """
    후위 표기된 문자열을 가지고 stack 이용해서 이항연산으로 계산
    :param result:
    :return:
    """
    stack = []
    for i in range(len(result)):
        if result[i] != '+' and result[i] != '*':
            stack.append(result[i])
        elif result[i] == '+':
            stack[-2] = int(stack[-1]) + int(stack[-2])
            stack.pop()
        elif result[i] == '*':
            stack[-2] = int(stack[-1]) * int(stack[-2])
            stack.pop()

    return stack[0]


def mid_to_post(N, inp):
    """
    중위 표기를 후위 표기로 바꾼 뒤, post_cal을 활용하여 계산값을 반환
    :param N: 중위 표기 식의 길이
    :param inp: 문자열로 표기된 중위 표기식
    :return: 변경된 후위표기식을 계산한 결과값
    """
    stack = []
    result = str()
    for i in range(N):
        if inp[i].isdigit():
            result += inp[i]
        elif len(stack) == 0:
            stack.append(inp[i])
        elif inp[i] == '(':
            stack.append(inp[i])
        elif inp[i] == '+':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack[-1]
                stack.pop()
            stack.append(inp[i])
        elif inp[i] == '*':
            while len(stack) > 0 and stack[-1] == '*':
                result += stack[-1]
                stack.pop()
            stack.append(inp[i])
        elif inp[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack[-1]
                stack.pop()
            stack.pop()
    while len(stack) > 0:
        result += stack[-1]
        stack.pop()

    return post_cal(result)


for tc in range(1, 11):
    N = int(input())
    inp = input()
    print("#%d %d" % (tc, mid_to_post(N, inp)))