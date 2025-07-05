def solution(a, b):
    answer = 0
    
    for i in range(b, 1, -1) :
        if a % i == 0 and b % i == 0 :
            a = int(a/i)
            b = int(b/i)
    tmp = b
    while tmp != 1 :
        if tmp % 2 == 0 :
            tmp = int(tmp / 2)
        elif tmp % 5 == 0 :
            tmp = int(tmp / 5)
        else :
            break
    if tmp == 1 :
        answer = 1
    else :
        answer = 2
    
    return answer