def markdown_parser(markdown):

    temp = markdown.split(' ')
    if len(temp) == 1:
        return markdown
    if markdown[0] != '#' and markdown[0] != ' ':
        return  markdown    

    count = 0
    index = 0
    for i in range(len(markdown)):
        if markdown[i] == "#":
            count += 1
        else:
            index = i + 1
            break
    
    if count >6:
        count = 6
    return_string = markdown[index:]
    return_string = return_string.strip()
    prefix = '<h' + str(count) + '>'
    suffix = '</h' + str(count) + '>'
    return prefix+ return_string + suffix
