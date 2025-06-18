def fac(number):
    gop = 1
    
    for k in range(1, number+1) :
        gop = gop * k
        
    return gop

def solution(n):
    answer = 0
    tmp = 0
    i = 0
    
    while n >= tmp :
        i = i + 1
        tmp = fac(i)
        answer = i-1
    
    
    
    
#     tmp = 1
#     i = 0
    
#     while n < tmp :
#         tmp = 1
#         i = i + 1
#         for k in range(1, i) :
#             tmp = tmp * k
#             print(k, i, tmp)
    
    return answer