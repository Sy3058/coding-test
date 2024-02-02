def solution(arr):
    if len(arr) > len(arr[0]):
        k = len(arr)-len(arr[0])
        for i in range (len(arr)):
            for j in range (k):
                arr[i].append(0)
    elif len(arr) < len(arr[0]):
        for i in range (len(arr[0])):
            for j in range (len(arr[0])-len(arr)):
                arr += [[0]*len(arr[0])]
    return arr