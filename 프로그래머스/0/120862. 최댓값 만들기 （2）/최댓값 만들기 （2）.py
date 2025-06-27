def solution(numbers):
    answer = 0
    
    numbers = sorted(numbers)
    
    max1 = numbers[0] * numbers[1]
    
    max2 = numbers[-1] * numbers[-2]
    
    answer = max(max1, max2)
    
    return answer