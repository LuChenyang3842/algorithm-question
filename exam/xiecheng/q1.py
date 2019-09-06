def  sortVersion(s1, s2):
    first = s1.split(".")
    second = s2.split(".")

    while len(first) <= 3:
        first.append('0')
    while len(second) <= 3:
        second.append('0')
    
    first = [int(x) for x in first]
    second = [int(x) for x in second]

    for i in range(3):
        if first[i] < second[i]:
            return  s1+ ","+ s2
        if second[i] < first[i]:
            return s2+ ","+ s1
    
    returns1+ ","+ s2


print(sortVersion('5.2.0','5.10'))

        
    

                
                
            