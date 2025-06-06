def solution(strArr):
    answer = []
    list1 = list()
    
    for i in strArr :
        if 'ad' not in i :
            list1.append(i)
            
    answer = list1
    
    return answer