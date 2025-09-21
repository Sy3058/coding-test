import sys
input = sys.stdin.readline

name, age, weight = input().split()

while name != "#":
  if int(age) > 17 or int(weight) >= 80:
    print(name, "Senior")
  else:
    print(name, "Junior")
  name, age, weight = input().split()