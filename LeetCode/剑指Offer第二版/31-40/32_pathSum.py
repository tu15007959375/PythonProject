from typing import List

from commonUtil import TreeNode, defineTestRoot


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        path = []
        res = []
        def recur(x, li):
            if x:
                li.append(x.val)
                if x.left:
                    recur(x.left, list(li))
                if x.right:
                    recur(x.right, list(li))
                if not x.left and not x.right:
                    path.append(list(li))

        recur(root, [])
        for ls in path:
            if sum(ls) == target:
                res.append(ls)
        return res

    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res


if __name__ == '__main__':
    sl = Solution()
    print(sl.pathSum2(defineTestRoot(), 17))
