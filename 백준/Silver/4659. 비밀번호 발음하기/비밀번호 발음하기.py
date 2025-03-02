import sys
input = sys.stdin.readline

# a, e, i, o, u 중 하나 포함
# 모음이 3개 혹은 자음이 3개 연속으로 올 수 없음
# 같은 글자는 연속으로 올 수 없음 (oo, ee 제외)

pw = input().strip()
vowel = ('a', 'e', 'i', 'o', 'u') # 모음

while pw != 'end':
  ccnt = 0
  vcnt = 0
  tvcnt = 0
  flag = True

  for i in range (len(pw)):
    if i != 0:
      if pw[i] == pw[i-1] and pw[i] not in ('e', 'o'):
        flag = False
        break
    if pw[i] in vowel:
      ccnt = 0
      vcnt += 1
      tvcnt += 1
    else:
      ccnt += 1
      vcnt = 0
    
    if ccnt == 3 or vcnt == 3:
      flag = False
      break
    
  if tvcnt == 0:
    flag = False
    
  if flag:
    print('<%s> is acceptable.'%(pw))
  else:
    print('<%s> is not acceptable.'%(pw))

  pw = input().strip()