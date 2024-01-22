import itertools

def perm(pos, cs, n):
    result = list(itertools.permutations(cs, n))
    for i in result:
        pos.append(''.join(i))
    return pos

def solution(babbling):
    cs = ['aya', 'ye', 'woo', 'ma']
    pos = []
    for i in range (1, 5):
        pos = perm(pos,cs,i)
    count = 0
    for i in babbling:
        if i in pos:
            count += 1
    return count