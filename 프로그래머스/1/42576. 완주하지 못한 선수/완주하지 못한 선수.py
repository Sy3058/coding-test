def solution(participant, completion):
    dic = {}
    for key in participant:
        dic[key] = dic.get(key, 0) + 1 # key가 있으면 key의 값에 1을 더하고 없으면 0에 1을 더한 값을 반환
    for ans in completion:
        dic[ans] -= 1
    answer = [i for i in dic if dic[i]>0]
    return answer[0]