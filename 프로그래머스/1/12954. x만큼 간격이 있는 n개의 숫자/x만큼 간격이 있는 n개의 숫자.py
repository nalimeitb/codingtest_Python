def solution(x, n):
    answer = []
    i = 0
    a = x
    
    while len(answer) != n :
        answer.append(a)
        a = a + x
    
    return answer