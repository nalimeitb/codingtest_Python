def solution(s):
    answer = 0
    list1 = s.split()
    
    for i in range(len(list1)) :
        if list1[i] == 'Z' :
            list1[i] = (-1) * int(list1[i-1])
    
    for i in list1 :
        answer = answer + int(i)
    
    
    return answer