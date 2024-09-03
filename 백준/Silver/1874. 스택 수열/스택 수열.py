import sys

n = int(sys.stdin.readline()) # 수열의 길이
sequence = [] # 수열이 입력될 리스트 생성

for _ in range(n):
  sequence.append(int(sys.stdin.readline()))

stack = []
answer = []
num = 1 # 수열에 추가되어야 하는 숫자
possible = True # 수열을 만드는 게 가능한 지 확인

for target in sequence:
  while num <= target: # target까지 stack에 num을 push
    stack.append(num) # stack에 num 추가
    answer.append("+") # push이므로 answer에 + 추가
    num += 1
  if stack[-1] == target: # stack의 가장 위에 있는 숫자와 target이 같다면 pop
    stack.pop()
    answer.append("-")
  else: # stack의 가장 마지막 수와 target이 동일하지 않다면 수열을 만들 수 없으므로 possible을 False로 바꾸고 진행 중지
    possible = False
    break

if possible:
  for ans in answer:
    print(ans, end="\n")
else:
  print("NO")