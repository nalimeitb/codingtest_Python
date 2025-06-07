def solution(myStr):
    answer = []
    
    myStr = myStr.replace('a', ' ')
    myStr = myStr.replace('b', ' ')
    myStr = myStr.replace('c', ' ')
    myStr = myStr.split(' ')    
    
    for i in myStr :
        if i != '' :
            answer.append(i)
    
    if answer == [] :
        answer = ["EMPTY"]
    
    return answer