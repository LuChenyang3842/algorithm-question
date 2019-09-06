#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        res_list = []
        for i in s:
            if i == ')' or i == ']' or i == '}':
                if not res_list:
                    return False
                out = res_list.pop()
                if not self.pair(out, i):
                    return False
            else:
                res_list.append(i)
        if res_list:
            return False
        return True

    
    def pair(self, a, b) -> bool:
        if a == '(' and b == ')':
            return True
        if a == '[' and b ==']':
            return True
        if a =='{' and b == "}":
            return True
        return False 
            

        

