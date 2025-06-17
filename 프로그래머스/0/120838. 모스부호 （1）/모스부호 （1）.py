def solution(letter):
    answer = ''
    list1 = list()
    
    morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    letter = letter.split()
    
    for i in range(len(letter)) :
        list1.append(morse[letter[i]])
        
    for k in list1 :
        answer = answer + k
    
    return answer