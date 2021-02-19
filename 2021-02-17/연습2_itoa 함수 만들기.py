num_int = 1234
num_list = []
while True:
    rem = num_int % 10
    num_list.append(rem)
    num_int = num_int // 10
    if num_int == 0:
        break
print(num_list)
num_list_reverse = []
for i in range(len(num_list)-1, -1, -1):
    num_list_reverse.append(num_list[i])
print(num_list_reverse)

num_str = ''.join(num_list_reverse)
print(num_str, type(num_str))


# 음수를 변환할 때는 어떤 고려사항이 필요?
