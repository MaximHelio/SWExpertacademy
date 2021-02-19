import sys
sys.stdin = open("input.txt", "r")

def pascal(line_list):
    line_list.append(0)
    line_list.insert(0, 0)
    arr = []
    for i in range(len(line_list)-1):
        arr.append(line_list[i]+line_list[i+1])
    result = str()
    for i in arr:
        result = result + str(i) +" "
    return result

for
print(pascal([1]))


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     line_list = [1]


# 재귀로