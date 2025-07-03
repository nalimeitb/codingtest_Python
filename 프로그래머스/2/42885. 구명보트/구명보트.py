def solution(people, limit):
    answer = 0
    people1 = sorted(people, reverse = True)
    left_i = 0
    right_i = len(people1) - 1
    
    while left_i <= right_i :
        if people1[left_i] + people1[right_i] <= limit :
            right_i = right_i - 1
        left_i = left_i + 1
        answer = answer + 1
                    
    # while people1 != [] :
    #     for i in range(len(people1)) :
    #         if people1[-1] + people[i] <= limit :
    #             people1.pop(i)
    #             people1.pop()
    #             answer = answer + 1
    #         else :
    #             people1.pop(i)
    #             answer = answer + 1        
    
    return answer