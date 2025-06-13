def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = denom1 * denom2
    b = numer1 * denom2 + numer2 * denom1
    
    while True :
        for i in range(a+1, 1, -1) :
            if b % i == 0 and a % i == 0 :
                a = int(a/i)
                b = int(b/i)
                print(a, b, i)
        else :
            break
    
    # for i in range(1, a) :
    #     if b % i == 0 and a % i == 0 :
    #         a = int(a / i)
    #         b = int(b / i)
    #         break
    
    if a == b :
        answer.append(1)
        answer.append(1)
    else :
        answer.append(b)
        answer.append(a)
    
    return answer