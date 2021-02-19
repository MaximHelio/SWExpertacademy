result = str(36)
cnt = 0
print(len(result))
for i in range(len(result)):
    if (result[i] == 3) or (result[i] == 6) or (result[i] == 9):
        cnt += 1
    print(cnt)