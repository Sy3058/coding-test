import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input()) # s의 길이
s = input().strip()

i = 0
cnt = 0
pn = 0 # 패턴 (IO)가 등장한 개수
while i < m - 1:
    # 'IOI' 패턴이 발견되면
    if s[i] == 'I' and s[i+1] == 'O' and i + 2 < m and s[i+2] == 'I':
        pn += 1
        i += 2 # 다음 앞의 패턴을 제거하고 뒤를 확인
    
        if pn == n:
            cnt += 1
            pn -= 1 # 겹치는 부분 제거
    
    else:
        i += 1
        pn = 0 # 패턴이 끊겼으니 초기화

print(cnt)