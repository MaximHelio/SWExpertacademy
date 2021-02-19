s1 = "gabagabagabagaba"
s2 = "gabaga"

cnt = 0
origin_s1 = len(s1)
while len(s1) >= len(s2):
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len(s2)] == s2:
            cnt += 1
            s1 = s1[i + len(s2)::]
result = origin_s1- len(s2) * cnt + cnt
print(result)