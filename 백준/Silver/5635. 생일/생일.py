n = int(input()) # number of students

info = {}
for _ in range (n):
  name, d, m, y = input().split()
  d, m, y = int(d), int(m), int(y)
  birth = '%04d%02d%02d'%(y,m,d)
  info[birth] = name

oldest = min(info.keys())
eldest = max(info.keys())
print(info[eldest])
print(info[oldest])