def solution(myString, pat):
    answer = 0
    k = 0
    a = len(pat)
    
    for i in range(len(myString)-a+1) :
        if pat == myString[i:i+a] :
            k = k + 1
    
    answer = k
    
    return answer