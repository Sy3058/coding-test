'''
import pandas as pd

def solution(strArr):
    length = []
    for i in strArr:
        length.append(len(i))
    id = list(set(length))
    df = pd.DataFrame([0]*len(id), index = id)
    for i in length:
        df[0][i] += 1
    return max(df[0])
'''
def solution(strArr):
    ans = [0]*31
    for i in strArr:
        ans[len(i)] += 1
    return max(ans)