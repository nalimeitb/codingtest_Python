def solution(array):
    answer = 0
    
    arrary = array.sort()
    
    answer = array[int((len(array)//2))]
    
    return answer