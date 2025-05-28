def solution(my_string, s, e):
    answer = ''
    my_string = list(my_string)
    
    answer1 = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    
    for i in range(len(answer1)) :
        answer = answer + answer1[i]
    
    return answer