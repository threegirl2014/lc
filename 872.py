class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = self.find_leaves(root1)
        leaves2 = self.find_leaves(root2)
        if len(leaves1) == len(leaves2):
            for leaf1, leaf2 in zip(leaves1, leaves2):
                if leaf1 != leaf2:
                    return False
            else:
                return True
        else:
            return False

    def find_leaves(self, root):
        leaves = []
        if root.left:
            leaves.extend(self.find_leaves(root.left))
        if root.right:
            leaves.extend(self.find_leaves(root.right))
        if not root.left and not root.right:
            return [root.val]
        return leaves

def dfs(node):
    if node:
        if not node.left and not node.right:
            yield node.val
        yield from dfs(node.left)
        yield from dfs(node.right)


def build_tree():
    l = [3,5,1,6,2,9,8,None, None,7,4]
    root = TreeNode(l.pop(0))
    tree_list = [root]
    while tree_list:
        node = tree_list.pop(0)
        try:
            left_val = l.pop(0)
        except IndexError:
            break
        else:
            if left_val is not None:
                node.left = TreeNode(left_val)
                tree_list.append(node.left)
        try:
            right_val = l.pop(0)
        except IndexError:
            break
        else:
            if right_val is not None:
                node.right = TreeNode(right_val)
                tree_list.append(node.right)
    return root


if __name__ == '__main__':
    solution = Solution()
    print(solution.find_leaves(build_tree()))

