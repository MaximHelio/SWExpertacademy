# 선택정렬
# 새로운 메모리 공간을 쓰는 것은 아니고, 기존의 메모리의 것을 갖다가 옮김
# 0, 1, 2, 3, ... N-2 N-1
# 최솟값을 찾아 맨 앞에 옮기는 작업을 N-1번 하면 됨
arr = [7, 6, 2, 8, 4]
N = len(arr)

# 내부의 for문부터 이해를 하고, 외부의 for문을 작성
# 시험 칠 때는 그냥 sort() 써!
# 코드를 보고 짜는 게 아니라, 온전히 내가 작성하는 것은 의미가 있음
# 어차피 결과를 보는 거니까!
# 모든 알고리즘 과목평가와 알고리즘은 3문제가 출제, 2문제는 코딩문제, 한 문제는 서술형
# 2 문제는 swea처럼 문제 지문과 입력_ 답, 출력식
# 하나는 서술형 문제
# 2시간 안에 풀 수 있는 문제가 주어짐!
# 문제 지문 읽고, 입력-출력 보고, 입력으로 읽어들어온다 치고....
#  1회
for i in range(0, N-1):
    idx = i
    for j in range(i+1, N):
        if arr[idx] > arr[j]:
            idx = j
    arr[0], arr[idx] = arr[idx], arr[0]
print(arr)

# # 2회
# idx = 1
# for j in range(idx+1, N):
#     if arr[idx] > arr[j]:
#         idx = j
# arr[1], arr[idx] = arr[idx], arr[1]
# print(arr)
#
# # 3회
# idx = 2
# for j in range(idx+1, N):
#     if arr[idx] > arr[j]:
#         idx = j
# arr[2], arr[idx] = arr[idx], arr[2]
# print(arr)
#
# # 4회 = N-1회
# idx = 3
# for j in range(idx+1, N):
#     if arr[idx] > arr[j]:
#         idx = j
# arr[3], arr[idx] = arr[idx], arr[3]
# print(arr)

