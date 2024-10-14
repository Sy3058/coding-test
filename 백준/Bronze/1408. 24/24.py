now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

def to_sec(time):
  return time[0]*3600 + time[1]*60 + time[2]

def to_ans(time):
  h = time//3600
  ms = time%3600
  m = ms//60
  s = ms%60
  return [h, m, s]

now = to_sec(now)
start = to_sec(start)

if start < now:
  start += 3600*24

rest = start - now
ans = to_ans(rest)

print('%02d:%02d:%02d'%(ans[0], ans[1], ans[2]))