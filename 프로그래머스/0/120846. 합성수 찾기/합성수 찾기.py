def solution(n):
    answer = 0
    list1 = list()
    
    for i in range(1, n+1, 1) :
        j = 0
        for k in range(1, i+1, 1) :
            if i % k == 0 :
                j = j + 1
                if j >= 3 :
                    list1.append(i)
                    break
    
    answer = len(list1)
    
    return answer