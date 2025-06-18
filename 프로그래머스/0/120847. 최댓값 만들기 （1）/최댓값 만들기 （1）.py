def solution(numbers):
    answer = 0
    list1 = list()
    
    for i in range(len(numbers)) :
        for k in range(i+1, len(numbers)) :
            list1.append(numbers[i]*numbers[k])
    
    answer = max(list1)
    
    return answer