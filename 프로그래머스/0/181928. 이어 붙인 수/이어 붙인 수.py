def solution(num_list):
    answer = 0
    hol = ''
    jak = ''
    for i in range(len(num_list)) :
        if num_list[i] % 2 == 0 :
            jak = jak + str(num_list[i])
        else :
            hol = hol + str(num_list[i])
            
    answer = int(hol) + int(jak)
    return answer