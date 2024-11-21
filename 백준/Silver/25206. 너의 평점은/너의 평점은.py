import sys

courses = []
grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
ghap = 0 # sum grade
chap = 0 # sum credit

for i in range (20):
  n, c, g = sys.stdin.readline().split() # name, credit, grade
  c = float(c)
  
  if g != 'P':
    s = grade[g] # score
    ghap += s * c
    chap += c

avg = ghap / chap
print('%0.6f'%avg)