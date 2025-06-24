def solution(my_string):
    answer = 0
    
    my_string = my_string.split(" ")
    
    for i in range(len(my_string)) :
        if i == 0 :
            answer = int(my_string[i])
            
        elif my_string[i] == '+' :
            answer = answer + int(my_string[i+1])
        
        elif my_string[i] == '-' :
            answer = answer - int(my_string[i+1])
        
        else :
            continue
    
    return answer