def solution(s):
    answer = ''
    
    list1 = s.split()
    
    for i in range(len(list1)) :
        list1[i] = int(list1[i])
        
    answer = str(min(list1)) + " " + str(max(list1))
    
    return answer