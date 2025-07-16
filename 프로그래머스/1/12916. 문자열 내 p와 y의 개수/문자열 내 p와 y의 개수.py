def solution(s):
    answer = True
    a = 0
    b = 0
    
    for i in s :
        if i == "p" or i == "P" :
            a = a + 1
        elif i == "y" or i == "Y" :
            b = b + 1
    
    if a != b :
        answer = False
        
    return answer