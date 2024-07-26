def solution(nums):
    select = len(nums)/2
    nondup_nums = list(set(nums)) # 중복 없는 리스트 생성
    if len(nondup_nums) > select:
        answer = select
    else:
        answer = len(nondup_nums)
    return answer