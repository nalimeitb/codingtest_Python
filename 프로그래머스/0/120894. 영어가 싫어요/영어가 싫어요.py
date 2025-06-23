def solution(numbers):
    answer = 0
    
    dic1 = {'one' : '1', 
           'two' : '2', 
           'three' : '3',
           'four' : '4',
           'five' : '5',
           'six' : '6',
           'seven' : '7',
           'eight' : '8',
           'nine' : '9',
            'zero' : '0'
           }
    
    for i in dic1 :
        if i in numbers :
            numbers = numbers.replace(i, dic1[i])
    
    answer = int(numbers)
    
    return answer