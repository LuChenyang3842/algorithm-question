#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        self.stackA.append(node)
        # write code here
    def pop(self):
        if self.stackB == []:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        if self.stackB:
            return self.stackB.pop()
        else:
            return None
            
        # return xx