import sys
sys.stdin = open("input (10).txt", "r")

inp = input()
for letter in inp:
    if "a" <= letter <= "z":
       letter = letter.upper()
    print(letter, end="")