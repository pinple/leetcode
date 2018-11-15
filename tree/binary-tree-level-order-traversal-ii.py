"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = [[root.val]]
        queue = deque([root])
        while queue:
            levelans = []
            for _ in xrange(0, len(queue)):
                root = queue.popleft()
                if root.left:
                    levelans.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    levelans.append(root.right.val)
                    queue.append(root.right)
            if levelans:
                ans.append(levelans)
        return ans[::-1]
