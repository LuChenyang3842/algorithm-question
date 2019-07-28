#从上往下打印出二叉树的每个节点，同层节点从左至右打印。\

#@思路： 使用BFS Search的方法， 借助队列实现

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        helperList = [root]
        result = []
        while len(helperList):
            curr_node = helperList.pop(0)
            result.append(curr_node.val)
            if curr_node.left:
                helperList.append(curr_node.left)
            if curr_node.right:
                helperList.append(curr_node.right)
        return result
        
        # write code here