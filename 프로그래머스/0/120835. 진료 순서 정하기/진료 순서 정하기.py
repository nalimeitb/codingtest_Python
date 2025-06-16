def solution(emergency):
    answer = []
    dict1 = {}
    list1 = sorted(emergency, reverse = True)
    
    for i in range(len(list1)) :
        dict1[list1[i]] = i+1
        
    for i in emergency :
        answer.append(dict1[i])
    
    return answer