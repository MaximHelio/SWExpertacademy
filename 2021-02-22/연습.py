word_list = [[1], [1, 2, 3], [1, 0, 1]]
for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        if word_list[i][j] != 0:
            print(word_list[i][], end = " ")