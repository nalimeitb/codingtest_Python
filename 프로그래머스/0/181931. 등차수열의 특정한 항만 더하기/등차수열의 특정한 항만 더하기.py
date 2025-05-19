def solution(a, d, included):
    answer = 0
    
    n = len(included)
    lst = []
    b = 0
    for i in range(len(included)) :
        b = a+i*d
        lst.append(b)
    for i in range(len(included)) :
        if included[i] == True :
            answer = answer + lst[i]
        
    return answer