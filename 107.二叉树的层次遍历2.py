# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        ans = []
        curr = [root]
        while len(curr):
            ans_each = []
            temp = []
            for i in curr:
                ans_each.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            ans.append(ans_each)
            curr = temp
        return ans[::-1]



