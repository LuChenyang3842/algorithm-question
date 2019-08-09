#输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点
# （含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

class Solution:
    def __init__(self):
        self.max = 0
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot:
            self.findMax(pRoot,1)
        return self.max
        
    def findMax(self,root,num):
        if num > self.max:
            self.max = num
        if root.left:
            self.findMax(root.left,num+1)
        if root.right:
            self.findMax(root.right,num+1)