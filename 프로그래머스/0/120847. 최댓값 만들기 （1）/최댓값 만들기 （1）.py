def solution(numbers):
    answer = 0
    answer = max(numbers)
    
    max_index = numbers.index(max(numbers))
    numbers.pop(max_index)
    
    answer = answer * max(numbers)
    
    return answer