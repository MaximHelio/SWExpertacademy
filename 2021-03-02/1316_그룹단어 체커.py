N = int(input())
word_list = []
for _ in range(N):
    word_list.append(str(input()))

cnt = 0
for word in word_list:
    word_group = []
    for i in range(len(word)):
        word_group.append(word[i])

    if len(set(word_group)) == len(word_group):
        cnt += 1
    else:
        letter_cnt = 0
        for letter in word_group:
            if letter:
                letter_cnt += 1
            if letter_cnt >= 2:
                print(letter)

