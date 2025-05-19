def solution(num_list):
    answer = 0
    gop = 1
    hap = 0
    hapjegop = 0
    for i in range(len(num_list)) :
        gop = gop * num_list[i]
        hap = hap + num_list[i]
    hapjegop = hap**2    
    if gop < hapjegop :
        answer = 1
    elif gop > hapjegop :
        answer = 0
    
    return answer
