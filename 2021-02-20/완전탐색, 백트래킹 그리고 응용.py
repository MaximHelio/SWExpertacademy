# 1~7까지의 숫자카드가 있을 때, 이것을 나열할 수 있는 경우의 수를 출력

# 뽑는 게 반복

num_list = [i+1 for i in range(7)]
print(type(num_list))
arr = []
for num in num_list:
     while len(num_list) >= 0:
         if num not in arr:
             arr.append(num)
             num_list = num_list.remove(num)
     print(arr)
