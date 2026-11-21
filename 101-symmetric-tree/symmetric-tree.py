# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def same(self,p,q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val==q.val:
            return self.same(p.left,q.right) and self.same(p.right,q.left)
        return False
    def isSymmetric(self, root):
        if root==None:
            return True
        return self.same(root.left,root.right)