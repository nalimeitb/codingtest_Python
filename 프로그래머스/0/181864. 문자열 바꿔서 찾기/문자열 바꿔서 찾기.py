def solution(myString, pat):
    answer = 0
    
    myString = myString.replace('A', 'C')
    myString = myString.replace('B', 'A')
    myString = myString.replace('C', 'B')
    
    if pat in myString :
        answer = 1
    else :
        answer = 0
    
    return answer