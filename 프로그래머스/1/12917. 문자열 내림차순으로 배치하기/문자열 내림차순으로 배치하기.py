def solution(s):
    answer = ''
    
    s = list(s)
    
    s.sort()
    
    for i in range(len(s)-1, -1, -1) :
        answer = answer + s[i]
    
    return answer