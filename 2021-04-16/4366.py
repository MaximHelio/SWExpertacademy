import sys
sys.stdin = open('sample_input (3).txt')


T = int(input())
for tc in range(1, T+1):
    num1 = list(input()) # 2진수
    num2 = list(input()) # 3진수
    # 먼저 한 자리씩만 바꾸기
    # 2진수
    shift_list1 = []
    shift_list2 = []
    for i in range(len(num1)):
        temp1 = num1[:]
        if temp1[i] == '1':
            temp1[i] = '0'
        elif temp1[i] == '0':
            temp1[i] = '1'
        shift_list1.append(''.join(temp1))
    for i in range(len(num2)):
        temp2 = num2[:]
        if temp2[i] == '0':
            temp2[i] = '1'
            shift_list2.append(''.join(temp2))
            temp2[i] = '2'
            shift_list2.append(''.join(temp2))
        elif temp2[i] == '1':
            temp2[i] = '0'
            shift_list2.append(''.join(temp2))
            temp2[i] = '2'
            shift_list2.append(''.join(temp2))
        elif temp2[i] == '2':
            temp2[i] = '1'
            shift_list2.append(''.join(temp2))
            temp2[i] = '0'
            shift_list2.append(''.join(temp2))

    ten_list_num1 = []
    for s in shift_list1:
        s = s[::-1]
        ten = 0
        for i in range(len(s)):
            if i == 0:
                x = 1 if s[int(i)] == '1' else 0
                ten += x
            else:
                if s[i] == '1':
                    ten += (2 ** i)
        ten_list_num1.append(ten)

    ten_list_num2 = []
    for s in shift_list2:
        s = s[::-1]
        ten = 0
        for i in range(len(s)):
            ten += int(s[i]) * (3 ** i)
        ten_list_num2.append(ten)

    for a in ten_list_num1:
        for b in ten_list_num2:
            if a == b:
                ans = a
    print('#%d %d' %(tc, ans))