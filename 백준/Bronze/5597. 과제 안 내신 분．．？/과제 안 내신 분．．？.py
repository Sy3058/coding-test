import sys

students = []

for _ in range (28):
  s = int(sys.stdin.readline())
  students.append(s)

for i in range (1, 31):
  if i not in students:
    print(i)