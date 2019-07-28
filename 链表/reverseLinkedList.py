# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        
        prev = None
        while pHead:
            temp = pHead.next
            pHead.next = prev
            prev = pHead
            pHead = temp
        return prev