def solution(food):
    answer = ''
    
    for i in range(1,len(food), 1) :
        answer = answer + str(i) * (int(food[i]//2))
        
    reversed_answer = answer[::-1]
    
    # reversed_answer = ''.join(reversed(answer))
    
    answer = answer + '0' + reversed_answer
    
    
    
    return answer