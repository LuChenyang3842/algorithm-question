class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        slow = pHead
        fast = pHead.next
        while fast:
            if fast.val == slow.val:
                if fast.next:
                    fast = fast.next
                    slow.next = fast
                else:
                    fast = None
                    slow.next = None
        return pHead