def solution(my_string, m, c):
    answer = ''
    answer1 = list()
    i = 0
    
    while i * m < len(my_string) :
        answer1.append(my_string[i*m:(i+1)*m])
        i = i + 1
    
    for k in answer1 :
        answer = answer + k[c-1]
    
        
    return answer