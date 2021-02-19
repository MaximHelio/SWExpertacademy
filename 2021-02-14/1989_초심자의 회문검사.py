import sys
sys.stdin = open("input (3).txt", "r")

T = int(input())
for tc in range(1, T+1):
    word = input()
    if word == word[-1::-1]:
        print("1")
    else: print("0")