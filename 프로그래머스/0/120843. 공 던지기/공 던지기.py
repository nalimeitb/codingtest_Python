def solution(numbers, k):
    answer = 0
    
    while k * 2 > len(numbers) :
        numbers = numbers + numbers
        
    answer = numbers[(k-1)*2]
    
    return answer