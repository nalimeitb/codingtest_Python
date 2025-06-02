def solution(num_list, n):
    answer = []
    
    a = num_list[:n]
    b = num_list[n:]
    
    answer = b + a
    
    return answer