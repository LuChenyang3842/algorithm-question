#输入一个链表，输出该链表中倒数第k个结点。

#@方法
#两个指针
#第二个指针在第一个指针前进k次后再前进
#终止条件： 第一个指针为空时
class Solution:
    def FindKthToTail(self, head, k):
        first = head
        second = head
        if k == 0:
            return None
        for i in range(k):
            if first != None:
                first = first.next
            else:
                return None
        while first!= None:
            first = first.next
            second = second.next
        return second
        # write code here