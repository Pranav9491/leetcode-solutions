# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        ans=[]
        if root==None:
            return ans
        flag=True
        q=[]
        q.append(root)
        while len(q)>0:
            temp=[]
            n=len(q)
            for i in range(n):
                a=q.pop(0)
                if a.left != None:
                    q.append(a.left)
                if a.right != None:
                    q.append(a.right)
                temp.append(a.val)
            if flag:
                ans.append(temp)
                flag=False
            else:
                temp.reverse()
                ans.append(temp)
                flag=True
        return ans