def solution(my_string, num1, num2):
    answer = ''
    a = my_string[num1]
    b = my_string[num2]
    c = ''
    my_string = list(my_string)
    my_string[num2] = a
    my_string[num1] = b
    
    for i in my_string :
        answer = answer + i
    
    return answer