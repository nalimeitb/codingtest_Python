def solution(n):
    answer = ""
    list1 = list()
    
    n = list(str(n))
    n = sorted(n, reverse = True)
    
    for i in n :
        answer = answer + i
        
    answer = int(answer)
    
    return answer