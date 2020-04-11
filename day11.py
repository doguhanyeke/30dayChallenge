# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def helper(root: TreeNode) -> int:
            nonlocal diameter
            if root is None:
                return 0
            left_max = helper(root.left)
            right_max = helper(root.right)
            max_cur = left_max + right_max
            if max_cur > diameter:
                # print(max_cur, diameter)
                diameter = max_cur
            return max(left_max, right_max) + 1
        helper(root)

        return diameter


root = TreeNode(1)
# two = TreeNode(2)
# root.left = two
# three = TreeNode(3)
# root.right = three
# four = TreeNode(4)
# two.left = four
# five = TreeNode(5)
# two.right = five
s = Solution()
res = s.diameterOfBinaryTree(root)
print(res)

