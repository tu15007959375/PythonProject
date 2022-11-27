# Definition for a binary tree node.
import queue

from commonUtil import defineTestRoot


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True


def printTree(root: TreeNode):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


if __name__ == '__main__':
    root = defineTestRoot()
    sl = Solution()
    # printTree(root)
    print(sl.isSymmetric(root))
