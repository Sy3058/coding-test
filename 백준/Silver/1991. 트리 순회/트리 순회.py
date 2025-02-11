import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range (n):
  c, l, r = input().strip().split()
  tree[c] = (l, r)

def pre(node):
  if node == '.':
    return ""
  l, r = tree[node]
  return node + pre(l) + pre(r)

def io(node):
  if node == '.':
    return ""
  l, r = tree[node]
  return io(l) + node + io(r)

def post(node):
  if node == '.':
    return ""
  l, r = tree[node]
  return post(l) + post(r) + node

print(pre('A'))
print(io('A'))
print(post('A'))