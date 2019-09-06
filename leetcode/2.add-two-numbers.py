#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNum = []
        secondNum = []
        while l1:
            firstNum.append(l1.val)
            l1 = l1.next
        while l2:
            secondNum.append(l2.val)
            l2 = l2.next
        firstNum.reverse()
        secondNum.reverse()
        res = self.convert(firstNum) + self.convert(secondNum)
        resultList = [int(i) for i in str(res)]
        resultList.reverse()
        if not resultList:
            return None
        else:
            pNode = ListNode(resultList[0])
            temp = pNode
            for i in range(1,len(resultList)):
                temp.next = ListNode(resultList[i])
                temp = temp.next
            temp.next = None
            return pNode


    
    def convert(self, list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return res
        

