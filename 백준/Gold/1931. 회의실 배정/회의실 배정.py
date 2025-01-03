import sys
input = sys.stdin.readline

n = int(input())
meeting = []
mcnt = 0

for _ in range (n):
  s, e = map(int, input().split())
  meeting.append((s, e))

meeting.sort(key = lambda x:(x[1], x[0])) # 종료 시간이 빠른 순서대로 (동일하다면 시작 시간이 빠른 순서대로)

cnt = 0
end_time = 0

for s, e in meeting:
  if s >= end_time: # 끝나는 시간이 이전 회의의 종료 시간보다 긴 경우
    cnt += 1
    end_time = e

print(cnt)