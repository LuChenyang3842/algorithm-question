def  longestSubStrLength(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    matrix = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    max_match = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                matrix[i+1][j+1] = matrix[i][j] +1
                if matrix[i+1][j+1] > max_match:
                    max_match =matrix[i+1][j+1]
                    p = i+1
    
    return max_match
longestSubStrLength('abcd','abdde')
