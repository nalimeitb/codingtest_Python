def solution(array):
    answer = 0
    max = 0
    set1 = set(array)
    
    for i in set1 :
        if max < array.count(i) :
            max = array.count(i)
            answer = i
        elif max == array.count(i) :
            answer = -1
            
    
    return answer