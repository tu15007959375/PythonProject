# Definition for a binary tree node.
from commonUtil import printTree, defineTestRoot


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的镜像
# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            if root.left or root.right:
                root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root


if __name__ == '__main__':
    root = defineTestRoot()
    sl = Solution()
    # printTree(root)
    printTree(sl.mirrorTree(root))
