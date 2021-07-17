sentence = str(input())
for i in range(len(sentence)):
    result = ord(sentence[i]) - 64
    print(result, end=" ")