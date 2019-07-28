class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        head = ListNode(None)
        p = head
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                p.next = pHead2
                pHead2 = pHead2.next
            else:
                p.next = pHead1
                pHead1 = pHead1.next
            p =p.next
        if pHead1:
            p.next = pHead1
        if pHead2:
            p.next = pHead2
        
        return  head.next
            
        # write code here