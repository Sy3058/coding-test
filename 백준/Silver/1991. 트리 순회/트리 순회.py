import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range (n):
  c, l, r = input().strip().split()
  tree[c] = [l, r]

rpre, rio, rpost = [], [], []

def pre(node):
  if node not in rpre:
    rpre.append(node)
  if tree[node][0] != '.':
    rpre.append(tree[node][0])
    pre(tree[node][0])
  if tree[node][1] != '.':
    rpre.append(tree[node][1])
    pre(tree[node][1])
  return rpre

print(''.join(pre('A')))

def io(node):
  if tree[node][0] != '.':
    io(tree[node][0])
    if tree[node][0] not in rio:
      rio.append(tree[node][0])
  if node not in rio:
    rio.append(node)
  if tree[node][1] != '.':
    io(tree[node][1])
    if tree[node][1] not in rio:
      rio.append(tree[node][1])
  return rio
  
print(''.join(io('A')))

def post(node):
  if tree[node][0] != '.':
    post(tree[node][0])
    if tree[node][0] not in rpost:
      rpost.append(tree[node][0])
  if tree[node][1] != '.':
    post(tree[node][1])
    if tree[node][1] not in rpost:
      rpost.append(tree[node][1])
  if node not in rpost:
    rpost.append(node)
  return rpost

print(''.join(post('A')))