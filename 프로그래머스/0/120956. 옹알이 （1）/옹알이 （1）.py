def solution(babbling):
    answer = 0
    a = 'aya'
    b = 'ye'
    c = 'woo'
    d = 'ma'
    set1 = (a, b, c, d,
            a+b, b+a,
            a+c, c+a,
            a+d, d+a,
            b+c, c+b,
            b+d, d+b,
            c+d, d+c,
            a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a,
            a+b+d, a+d+b, b+a+d, b+d+a, d+a+b, d+b+a,
            a+c+d, a+d+c, c+a+d, c+d+a, d+a+c, d+c+a,
            b+c+d, b+d+c, c+b+d, c+d+b, d+b+c, d+c+b,
            a+b+c+d, a+b+d+c, a+c+b+d, a+c+d+b, a+d+b+c, a+d+c+b,
           b+a+c+d, b+a+d+c, b+c+a+d, b+c+d+a, b+d+a+c, b+d+c+a,
           c+a+b+d, c+a+d+b, c+b+a+d, c+b+d+a, c+d+a+b, c+d+b+a,
           d+a+b+c, d+a+c+b, d+b+a+c, d+b+c+a, d+c+a+b, d+c+b+a)
    
    count = 0
    
    for i in babbling :
        if i in set1 :
            count = count + 1
            
    answer = count
    
    return answer