import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range (n)]
words = list(set(words)) # 중복 제거
words.sort(key = lambda x:(len(x), x)) # 조건 1. x의 길이, 조건2. x

for i in range (len(words)): print(words[i])