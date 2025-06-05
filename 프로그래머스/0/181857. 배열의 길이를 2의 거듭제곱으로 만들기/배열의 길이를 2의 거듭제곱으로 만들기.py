def solution(arr):
    answer = arr
    a = len(arr)
    i = 0
    
    while True :
        if 2**i >= a :
            for i in range(2**i - a) :
                answer.append(0)
            break
        else :
            i = i + 1
            continue
    
    return answer