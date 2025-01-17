import sys
input = sys.stdin.readline

u = list(map(int, input().split()))
v = (u[0]**2 + u[1]**2 + u[2]**2 + u[3]**2 + u[4]**2)%10
print(v)