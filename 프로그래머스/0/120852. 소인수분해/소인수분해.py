def solution(n):
    answer = []
    list1 = list()
    
    while n != 1 :
        for i in range(2, n+1) :
            if n % i == 0 :
                n = int(n / i)
                list1.append(i)
                break
            
    set1 = set(list1)
    # answer = list(set1)
    answer = sorted(list(set1))
    
    
    return answer