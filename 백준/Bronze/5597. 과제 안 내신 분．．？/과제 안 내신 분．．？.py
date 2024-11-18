import sys

students = set([i for i in range (1, 31)])
check = []
for _ in range (28):
  s = int(sys.stdin.readline())
  check.append(s)

check = set(check)
missing = list(students - check)

print(min(missing))
print(max(missing))