def solution(arr, flag):
    x = []
    for i in range (len(flag)):
        if flag[i] == True:
            for j in range (arr[i]*2):
                x.append(arr[i])
        else:
            for j in range (arr[i]):
                x.pop()
    return x