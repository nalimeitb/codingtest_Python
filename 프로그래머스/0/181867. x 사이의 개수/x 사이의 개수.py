def solution(myString):
    answer = []
    list1 = list()
    list2 = list()
    
    list1 = myString.split('x')
    
    for i in range(len(list1)) :
        list2.append(len(list1[i]))
        
    answer = list2
    
    
    return answer