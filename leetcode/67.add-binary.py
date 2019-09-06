#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [i for i in a]
        b = [i for i in b]
        a = a[::-1]
        b = b[::-1]
        if len(a) > len (b):
            for i in range (len(a)- len(b)):
                b.append(0)
        
        if len(b) > len(a):
            for i in range(len(b) - len(a)):
                a.append(0)
        
        result = []
        flag = '0'
        for i in range(len(a)):
            if self.plus(a[i], b[i]) == '0':
                if flag == '0':
                    result.append('0')
                elif flag == '1':
                    result.append('1')
                    flag == '0'
            if self.plus(a[i], b[i]) == '1':
                if flag == '0':
                    result.append('1')
                elif flag == '1':
                    result.append('0')
                    flag == '1'
            if self.plus(a[i], b[i]) == '2':
                if flag == '0':
                    result.append('0')
                    flag = '1'
                elif flag == '1':
                    result.append('0')
                    flag == '1'
    
    def plus(self, first, second):
        if first == '1' and second == '1':
            return '2'
        if first =='0' and second == '0':
            return '0'
        return '1'

                



        
        

