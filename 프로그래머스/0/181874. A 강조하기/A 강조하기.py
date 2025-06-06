def solution(myString):
    answer = ''
    list1 = list(myString)
    
    for i in range(len(list1)) :
        if list1[i] == 'a' :
            list1[i] = 'A'
            answer = answer + list1[i]
        elif list1[i] == 'A' :
            list1[i] = 'A'
            answer = answer + list1[i]
        else :
            list1[i] = list1[i].lower()
            answer = answer + list1[i]
    
    
    return answer