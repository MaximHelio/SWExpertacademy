import sys
sys.stdin = open("sample_input.txt", "r")


def braket(sentence):
    parenthesis = []
    for letter in sentence:
        if letter == '(' or letter == ')' or letter == '{' or letter == '}':
            parenthesis.append(letter)


    stack = []
    for data in parenthesis:
        if data == '(' or data == '{':
            stack.append(data)
        elif data == '}':
            if len(stack) == 0: return 0
            elif stack[-1] == '{':
                stack.pop()
            else: return 0
        elif data == ')':
            if len(stack)== 0: return 0
            elif stack[-1] == '(':
                stack.pop()
            else: return 0

    if len(stack) == 0: return 1
    else: return 0

T = int(input())
for tc in range(1, T + 1):
    sentence = str(input())
    print("#%d %d" %(tc, braket(sentence)))



# def check_braket(text):
#     stack = []
#     for idx, letter in enumerate(text):
#         if letter == '(':
#             stack.append(idx)
#         elif letter == ')':
#             if stack:
#                 stack.pop()
#             else:
#                 stack.append(idx)
#                 return stack
#     return stack
# print(check_braket('2.4 + 23/12 + (3.141592 * .21))'))
#
# def braket(sentence):
#     stack = []
#     # sentence 문자열의 원소들을 검사
#     for letter in sentence:
#         # stack이 비어있을 때 여는 괄호가 나오면 추가, 닫는 괄호가 나오면 False
#         if len(stack) == 0:
#             if letter == '(' or letter == '{':
#                 stack.append(letter)
#             else:
#                 return 0
#         # stack이 비어있지 않을 때 여는 괄호가 나오면 추가, 닫는 괄호가 나오면 pop
#         elif letter == '(' or letter == '{':
#             stack.append(letter)
#         elif letter == ')':
#             if stack[-1] == '(':
#                 stack.pop()
#             else:
#                 return 0
#         elif letter == '}':
#             if stack[-1] == '{':
#                 stack.pop()
#             else:
#                 return 0
#
#     # 검사가 끝난 후, stack이 비어있으면 짝이 잘 맞는 것
#
#
#     if len(stack) == 0:
#         return 1
#     else:
#         return 0
#
# T = int(input())
# for tc in range(1, T + 1):
#     sentence = str(input())
#     print("#%d %d" % (tc, braket(sentence)))
#
# for i in range(len(arr)):
#     if arr[i] == '{' or arr[i] == '(':
#         스택에 push
#     # if arr[i] == '(':
#     #     스택에 push
#     elif arr[i] == '}':
#         if len(스택) > 0 and 스택에 pop해서 =='{':
#
#     else: