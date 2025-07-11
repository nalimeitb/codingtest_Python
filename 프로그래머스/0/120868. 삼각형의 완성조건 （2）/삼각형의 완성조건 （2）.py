def solution(sides):
    answer = 0
    
    sum1 = sides[0] + sides[1]
    small1 = min(sides)
    big1 = max(sides)
    
    tmp = big1 + 1
    while tmp < sum1 :
        answer = answer + 1
        tmp = tmp + 1
    
    tmp = big1 - small1 + 1
    while tmp <= big1 :
        answer = answer + 1
        tmp = tmp + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     tmp1 = max(sides) - min(sides)
#     tmp2 = max(sides) + min(sides) - 1
    
#     while True :
#         tmp1 = tmp1 + 1
#         answer = answer + 1
#         if tmp1 == max(sides) :
#             break
            
#     while tmp2 > max(sides) :
#         tmp2 = tmp2 - 1
#         answer = answer + 1








    
    return answer