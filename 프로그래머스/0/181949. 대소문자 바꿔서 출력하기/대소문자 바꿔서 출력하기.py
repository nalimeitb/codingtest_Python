str = input()
modified_str = ""

for i in range(len(str)) :
    if str[i].isupper() :
        modified_str = modified_str + str[i].lower()
    else :
        modified_str = modified_str + str[i].upper()
        
print(modified_str)
