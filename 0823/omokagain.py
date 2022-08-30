import sys
sys.stdin = open('omok_input (1).txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input().strip())) for _ in range(N)]
    lst = []
