# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第
# 一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

from collections import Counter
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        charList = list(s)
        ctr =  Counter(charList)
        for i in range(len(charList)):
            if ctr[charList[i]] == 1:
                return i
        return -1