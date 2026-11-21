# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []

        q = [root]
        ans = []

        while len(q) > 0:
            temp = []
            n = len(q)

            for i in range(n):
                a = q.pop(0)
                temp.append(a.val)

                if a.left != None:
                    q.append(a.left)

                if a.right != None:
                    q.append(a.right)

            ans.append(temp)

        ans.reverse()
        return ans