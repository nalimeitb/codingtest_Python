def solution(numLog):
    answer = ''
    
    a = []
    for i in range(1, len(numLog)) :
        if numLog[i-1] == numLog[i] - 1 :
            a.append('w')
        elif numLog[i-1] == numLog[i] + 1 :
            a.append('s')
        elif numLog[i-1] == numLog[i] - 10 :
            a.append('d')
        elif numLog[i-1] == numLog[i] + 10 :
            a.append('a')
            
    for i in range(len(a)) :
        answer = answer + str(a[i])
    
    return answer