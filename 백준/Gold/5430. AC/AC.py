from collections import deque

T = int(input()) # 테스트 케이스의 개수

for _ in range (T):
  p = input() # 수행할 함수 p
  n = int(input()) # 배열에 들어있는 수의 개수
  arr = deque(input().rstrip()[1:-1].split(','))
  if n == 0:
    arr = deque()

  flag = False
  cnt = 0 # 뒤집힌 횟수

  for c in p: # 실행할 명령
    if c == 'R':
      cnt += 1
    elif c == 'D':
      if arr:
        if cnt % 2 == 0: # 짝수번 뒤집었다면 원상태
          arr.popleft()
        else: # 홀수번 뒤집었다면 맨 뒤에서 뽑아내는 것이 뒤집고 앞에서 뽑는 것과 동일
          arr.pop()
      else:
        flag = True
        break
  
  if flag:
    print('error')
  else:
    if cnt % 2 == 0:
      print('['+','.join(arr)+']')
    else:
      arr.reverse()
      print('['+','.join(arr)+']')