# 정수 => 문자열 : str()
# 문자열 => 정수 : int()

# a = ['1', '2', '3']
# alst = "123"
# for a in alst:
#     alst[1] = '3'
#     print(a)
#
# for a in lst:
#     print(a)

# 리스트 => 문자열 : ''.join(alst)
# 문자열 => 리스트 : 문자열을 바꾸고 싶을 때 list(lst)

# ord, chr 써도 됨!



#1. 리스트로 바꿔서 교환
# def string_reverse(s):
#     s_list = list(s)
#     s_reverse_list = []
#     for i in range(len(s_list)-1, -1, -1):
#         s_reverse_list.append(s_list[i])
#
#     s_reverse = ''.join(s_reverse_list)
#     return s_reverse
# s = str(input())
# print(string_reverse(s), type(string_reverse(s)))

# 2. 새로운 문자열 만들어서 역으로 읽는 것
# def string_reverse(s):
#     new_s = str()
#     for i in range(len(s)-1, -1, -1):
#         new_s += s[i]
#     return new_s
# s = str(input())
# print(string_reverse(s))