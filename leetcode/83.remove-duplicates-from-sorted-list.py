#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            fast = head.next
            slow = head
            while fast:
                if fast.val == slow.val:
                    fast = fast.next
                    if not fast:
                        slow.next = fast
                elif fast.val != slow.val:
                    temp = fast
                    slow.next = temp
                    slow = slow.next
                    fast = fast.next
        return head


        

