def solution(a, b, c, d):
    answer = 0
    
    if a == b == c == d :
        answer = a * 1111
        
    elif a == b == c != d :
        answer = (10 * a + d)**2
        
    elif a == b == d != c :
        answer = (10 * a + c)**2
        
    elif a == c == d != b :
        answer = (10 * a + b)**2
        
    elif b == c == d != a :
        answer = (10 * b + a)**2
        
    elif a == b and c == d and a != c :
        answer = (a + c) * abs(a-c)
        
    elif a == c and b == d and a != b :
        answer = (a + b) * abs(a-b)
        
    elif a == d and b == c and a != b :
        answer = (a + b) * abs(a-b)
        
    elif a == b and c != d :
        answer = c * d
        
    elif a == c and b != d :
        answer = b * d
        
    elif a == d and b != c :
        answer = b * c
        
    elif b == d and a != c :
        answer = a * c
        
    elif b == c and a != d :
        answer = a * d
        
    elif c == d and a != b :
        answer = a * b
        
    else :
        answer = min(a, b, c, d)
    
    
    return answer