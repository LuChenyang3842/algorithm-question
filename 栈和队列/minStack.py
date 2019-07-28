#定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.min_stack) ==0:
            self.min_stack.append(node)
        else:
            if self.min_stack[-1] >= node:
                self.min_stack.append(node)
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
        # write code here
    def top(self):
        return self.stack[-1]
        # write code here
    def min(self):
        return self.min_stack[-1]
        # write code here

test = Solution()
test.push(1)
test.push(2)
print(test.min())