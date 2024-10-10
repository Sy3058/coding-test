t = int(input()) # test case

for _ in range (t):
  Yon = 0 # score of Yonsei
  Kor = 0 # score of Korea
  for _ in range (9):
    y, k = map(int, input().split()) # score of Yonsei and Korea
    Yon += y
    Kor += k
  if Yon > Kor:
    print('Yonsei')
  elif Yon < Kor:
    print('Korea')
  else:
    print('Draw')