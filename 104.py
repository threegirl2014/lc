# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return 1 + max(left_max, right_max)


if __name__ == '__main__':
    node_15 = TreeNode(15)
    node_7 = TreeNode(7)
    node_20 = TreeNode(20)
    node_9 = TreeNode(9)
    node_3 = TreeNode(3)
    node_3.left = node_9
    node_3.right = node_20
    node_20.left = node_15
    node_20.right = node_7
    solution = Solution()
    print(solution.maxDepth(node_3))
