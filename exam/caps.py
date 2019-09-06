def numsOfKey(input_string):
    sum = len(input_string)
    flag = 0
    for i in range(len(input_string)):
        if input_string[i].islower() and flag == 1:
            if i + 1 < len(input_string) and  input_string[i+1].islower():
                flag = 0
            sum +=1
        elif input_string[i].isupper() and flag == 0:
            if i + 1< len(input_string) and input_string[i+1].isupper():
                flag = 1
            sum +=1
    return sum

print(numsOfKey('AaAAaA'))

            

