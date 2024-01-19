def solution(arr, queries):
    result = []
    sol = []
    for query in queries:
        s = query [0]
        e = query [1]
        k = query [2]
        
        for i in range(s, e+1, 1):
            if arr[i] > k:
                sol.append(arr[i])
        if len(sol) == 0:
            result.append(-1)
        else:
            result.append(min(sol))
        sol = []
    return result