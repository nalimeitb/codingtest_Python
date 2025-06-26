def solution(dots):
    answer = 0
    
    # answer = abs(dots[0][0] - dots[1][0]) * abs(dots[1][1] - dots[2][1])
    
    list1 = list()
    list2 = list()
    
    for x,y in dots :
        list1.append(x)
        list2.append(y)
        
    list1 = list(set(list1))
    list2 = list(set(list2))
    
    a = abs(list1[0] - list1[1])
    b = abs(list2[0] - list2[1])
    
    answer = a*b
    
    return answer