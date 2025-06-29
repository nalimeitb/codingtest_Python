def solution(my_string):
    answer = 0
    str1 = ''
    list1 = list()
    set1 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    
    for i in range(len(my_string)) :
        if my_string[i] in set1 :
            str1 = str1 + my_string[i]
        else :
            str1 = str1 + ' '
    
    list1 = str1.split(" ")
    
    for i in list1 :
        if i == '' :
            continue
        else :
            answer = answer + int(i)
    
    
    
    return answer