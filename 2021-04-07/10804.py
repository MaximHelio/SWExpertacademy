T = int(input())
for tc in range(1, T+1):
    word = input()
    answer = str()
    word_reverse = word[::-1]
    for letter in word_reverse:
        if letter == 'b':
            answer += 'd'
        elif letter == 'd':
            answer += 'b'
        elif letter == 'p':
            answer += 'q'
        else:
            answer += 'p'

    print('#%d %s' %(tc, answer))
#  T = int(input())
# for tc in range(1, T+1):
#     word = str(input())
#     word_reverse = word[::-1]
#     for letter in word_reverse:
#         if letter == "p":
#             letter = "q"
#         elif letter == "q":
#             letter = "p"
#         elif letter == "b":
#             letter = "d"
#         elif letter == "d":
#             letter = "b"
#     print('#%d %d' %(tc, word_reverse))