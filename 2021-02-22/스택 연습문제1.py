#############스택을 구현하기################
# stack = []
# data = [i for i in range(10)]
# for i in range(len(data)):
#     stack.append(data[i])
# print(stack)
# print(stack.pop())
# print(stack.pop())
class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items


stk = stack()
print(stk)
print(stk.isEmpty())
stk.push(1)
stk.push(2)
print(stk.pop())
print(stk.pop())
print(stk.isEmpty())

# 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고, 다시 3번 꺼내서 출력해봅니다.