import sys

a, b = map(int, sys.stdin.readline().split())
s1 = set(map(int, sys.stdin.readline().split()))
s2 = set(map(int, sys.stdin.readline().split()))
s3 = s1 ^ s2 # 대칭 차집합
print(len(s3))