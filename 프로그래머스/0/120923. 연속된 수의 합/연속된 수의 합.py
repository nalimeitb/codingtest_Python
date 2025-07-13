def solution(num, total):
    answer = []
    
    for i in range(-50, 1000, 1) :
        sum1 = 0
        answer = []
        for j in range(i, i + num) :
            sum1 = sum1 + j
            answer.append(j)
        if sum1 == total :
            break
    
    return answer