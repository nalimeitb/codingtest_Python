def solution(arr1, arr2):
    answer = []
    
    k = 0
    for x,y in zip(arr1, arr2) :
        list1 = x+y
        answer.append([])
        
        for i in range(0, int(len(list1)/2)) :
            answer[k].append(list1[i] + list1[i+len(arr1[k])])
            
        k = k + 1
    
    
    return answer