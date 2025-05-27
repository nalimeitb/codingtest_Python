def solution(my_string, queries):
    answer = ''
    answer1 = list(my_string)
    
    for s,e in queries :
        answer1 = answer1[:s] + answer1[s:e+1][::-1] + answer1[e+1:]
    
    for i in range(len(answer1)) :
        answer = answer + answer1[i]
        
            
    return answer