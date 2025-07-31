def solution(nums):
    answer = 0
    
    nums_set = set(nums)
    
    halflen = len(nums) / 2
    
    if halflen < len(nums_set) :
        answer = halflen
    else :
        answer = len(nums_set)
    
    return answer