def solution(my_string):
    answer = []
    
    set = ("0", "1", "2", "3", "4", '5', "6", "7", "8", "9")
    
    for i in my_string :
        if i in set :
            answer.append(int(i))
    
    answer.sort()
    
    return answer