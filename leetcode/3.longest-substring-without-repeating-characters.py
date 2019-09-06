#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = []
        res.append([s[0]])
        for i in range(1,len(s)):
            if s[i] not in res[i-1]:
                temp = res[i-1]
                temp.append(s[i])
                res.append(temp)
            else:
                temp = []
                temp.append(s[i])
                for j in range(len(res[i-1])-1, -1,-1):
                    if res[i-1][j] == s[i]:
                        break
                    temp.append(res[i-1][j]) 
                temp.reverse()
                res.append(temp)
        
        result = []
        maxLen = 0
        for li in res:
            if len(li) > maxLen:
                maxLen = len(li)
                result = li
        
        result = ''.join(result)
        return maxLen


            



        

