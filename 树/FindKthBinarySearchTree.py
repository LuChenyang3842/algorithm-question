# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， 
# （5，3，7，2，4，6，8） 中，按结点数值大小顺序第三小结点的值为4。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        global res
        res = []
        self.sortTreeNode(pRoot)
        if  k<=0 or len(res)<k:
            return None
        return res[k-1]
        
    def sortTreeNode(self, midroot):
        if midRoot:
            self.sortTreeNode(midRoot.left)
            res.append(midroot)
            self.sortTreeNode(midRoot.right)