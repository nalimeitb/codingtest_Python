def solution(people, limit):
    answer = 0
    people1 = sorted(people, reverse = True)
    people2 = sorted(people)
    
    while people != [] :
        for i in range(len(people1)) :
            for k in range(len(people2)) :
                if people[i] + people[k] <= limit :
                    people1.remove(people1[i])
                    people2.remove(people2[k])
                    answer = answer + 1
            break
        
    
    # while len(people) != 0 :
        
    
    return answer