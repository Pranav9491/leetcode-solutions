# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        c = 0
        if root == None:
            return 0

        q = []
        q.append(root)

        while len(q) > 0:
            n = len(q)

            for i in range(n):
                a = q.pop(0)

                if a.left != None:
                    q.append(a.left)

                if a.right != None:
                    q.append(a.right)

            c += 1

        return c