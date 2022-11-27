from typing import List

from commonUtil import TreeNode, defineTestRoot


# 从上到下打印二叉树
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:

            nowNode = queue.pop(0)
            res.append(nowNode.val)
            if nowNode.left:
                queue.append(nowNode.left)
            if nowNode.right:
                queue.append(nowNode.right)

        return res


if __name__ == '__main__':
    sl = Solution()
    root = defineTestRoot()
    print(sl.levelOrder(root))
