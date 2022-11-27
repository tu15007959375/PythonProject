from typing import List

from commonUtil import TreeNode, defineTestRoot


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                nowNode = queue.pop(0)
                tmp.append(nowNode.val)
                if nowNode.left:
                    queue.append(nowNode.left)
                if nowNode.right:
                    queue.append(nowNode.right)
            res.append(tmp)

        return res


if __name__ == '__main__':
    sl = Solution()
    print(sl.levelOrder(defineTestRoot()))
