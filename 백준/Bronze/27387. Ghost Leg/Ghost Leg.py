import sys
input = sys.stdin.readline

"""
각 높이마다 가로로 길이 하나씩 있음
element를 [0, 1, 2, 3, ..., n]로 두고 a와 a+1의 위치를 스위치
--> 높이별로 rung에 따라 element의 위치를 교환
"""
n, m = map(int, input().split())
elements = [i for i in range (n+1)]
for _ in range (m):
    a = int(input())
    elements[a], elements[a+1] = elements[a+1], elements[a]

for i in range (1, n+1):
    print(elements[i])