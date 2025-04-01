import sys
input = sys.stdin.readline

s = input().strip()
z = [x for x in s.split('1') if x != ''] # 문자열을 1로 분할하면 0만 남은 리스트가 생김 그중에서 ''가 아닌 값만 리스트로 만들면 0으로 시작하는 부분들만 남음
o = [x for x in s.split('0') if x != '']

print(min(len(z), len(o)))