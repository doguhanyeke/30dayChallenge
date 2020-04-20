from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        lst_size = len(preorder)
        if lst_size == 0:
            return "null"

        def helper(i, j):
            if i > j or i >= lst_size or j >= lst_size:
                return
            else:
                root = TreeNode(preorder[i])

                if i == j:
                    return root

                print(i, j)
                index = j + 1
                for k in range(i+1, j+1, 1):
                    if preorder[k] > root.val:
                        index = k
                        break
                print("index:", index)

                root.left = helper(i+1, index - 1)
                root.right = helper(index, j)

                return root

        root = helper(0, lst_size-1)
        return root


def tree_traversal(root):
    if root:
        print(root.val)
        tree_traversal(root.left)
        tree_traversal(root.right)
    else:
        print("null")


s = Solution()
preorder = [15, 13, 12, 18]
root = s.bstFromPreorder(preorder)
tree_traversal(root)


