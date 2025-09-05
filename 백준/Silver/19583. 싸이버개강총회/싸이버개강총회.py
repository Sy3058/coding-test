import sys

# 개강총회 시작 시간 (22:00이라면 22:00에 채팅한 사람도 포함) 이전에 대화를 한 사람은 제 시간에 입장
# 개강총회 끝 ~ 스트리밍 끝 사이에 있는 사람은 제 시간에 퇴장

def time_to_minute(time):
  # time = hh:mm
  h = time[:2] # hh
  m = time[3:] # mm
  return int(h) * 60 + int(m)

s, e, q = input().split() # 개강 총회를 시작한 시간, 끝낸 시간, 스트리밍을 끝낸 시간
# 계산 편의를 위해 시간을 모두 분으로 통일
start = time_to_minute(s)
end = time_to_minute(e)
st_end = time_to_minute(q)

enter_set = set() # 개강 총회 시작 전에 채팅한 사람
exit_set = set() # 개강 총회 끝난 후 ~ 스트리밍 끝나기 전에 채팅한 사람

records = sys.stdin.read().splitlines() # 마지막 줄까지 모든 입력을 받고 개행문자를 기준으로 리스트로 나눔
for record in records:
  strtime, name = record.split()
  time = time_to_minute(strtime)
  if time <= start:
    enter_set.add(name)
  
  elif end <= time <= st_end:
    exit_set.add(name)

check_set = enter_set & exit_set # 양쪽에 다 있는 사람
print(len(check_set))