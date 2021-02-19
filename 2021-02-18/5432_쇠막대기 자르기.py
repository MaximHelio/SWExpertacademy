import sys
sys.stdin = open("sample_input (5).txt", "r")

T = int(input())
for tc in range(1, T+1):
    rough_laser = str(input())
    laser = rough_laser[1: len(rough_laser)-1]
    for i in range(len(laser)):

