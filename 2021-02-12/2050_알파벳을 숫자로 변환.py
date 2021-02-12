import sys
sys.stdin = open("input.txt", "r")

inp = input()
for i in range(len(inp)):
    print(ord(inp[i])-64, end=" ")