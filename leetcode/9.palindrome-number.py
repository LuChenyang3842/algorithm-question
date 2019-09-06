#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        num_list = [char for char in num]
        reverse_num_list = num_list[::-1]
        for i in range(len(num_list)):
            if num_list[i] != reverse_num_list[i]:
                return False
        return True

