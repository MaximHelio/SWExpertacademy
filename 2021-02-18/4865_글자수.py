import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 =list(set(input()))
    str2 = str(input())
    arr = []
    for letter2 in str2:
        if letter2 in str1: arr.append(letter2)
    str1_dict = {}
    for letter in arr:
        if letter in str1_dict:
            str1_dict[letter] += 1
        else: str1_dict[letter] = 1
    lst = list(str1_dict.values())
    print("#%d %d" %(tc, max(lst)))
# 딕셔너리 이용

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    #str1  각 문자의 카운트를 세기 위함
    cnt = [0] * len(str1)

    # str1 길이만큼 순회
    for i in range(len(str1)):
        # str1[i]가 str2에 몇 개 들어있는지 체크
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt[i] += 1
    ans = 0
    #가장 큰 값 찾기
    for i in range(len(cnt)):
        if ans < cnt[i]:
            ans = cnt[i]
    # ans = max(cnt)

    print("#{} {}".format(tc, ans))

###############
# 만약 주어진 문자가 모두 대문자만 들어온다면!!
for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()

    check_arr = [0] * 26 #str1에 해당 글자가 있는지 체크
    count_arr = [0] * 26 # 해당 글자 카운트

    # str1을 순회하면서 알파벳 체크
    for i in str1:
        check_arr[ord(i)-ord('A')] = 1 # 0~25까지의 인덱스

    # 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord(i)-ord('A')]:
            count_arr[ord(i)-65] += 1
    print("#{} {}",format(tc, max(count_arr)))