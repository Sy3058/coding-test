def solution(diffs, times, limit):
    low, high = 1, max(diffs)
    
    def solve(level):
        total_time = 0
        for i in range (len(diffs)):
            if i == 0:
                total_time += times[i]
            else:
                if diffs[i] <= level:
                    total_time += times[i]
                else:
                    error = diffs[i] - level
                    total_time += error * (times[i] + times[i-1]) + times[i]
            if total_time > limit:
                return False
        return total_time <= limit
    
    while low <= high: # low를 올리거나 high를 낮추면서 이분 탐색, low > high가 되면 끝
        mid = (low+high) // 2
        if solve(mid):
            high = mid - 1 # tt가 limit보다 작다면 숙련도가 더 낮아져도 괜찮음
        else:
            low = mid + 1
    return low