# 二叉搜索树的后续遍历数列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        if len(postorder) == 1 or len(postorder) == 2:
            return True
        pos = 1001
        root = postorder[-1]
        for i in range(len(postorder)):
            if pos == 1001 and postorder[i] > root:
                pos = i

            if i > pos and postorder[i] < root:
                return False
        if pos == 1001 or pos == 0:
            return self.verifyPostorder(postorder[0:-1])

        return self.verifyPostorder(postorder[0: pos]) and self.verifyPostorder(postorder[pos + 1:])

    def verifyPostorder2(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


if __name__ == '__main__':
    sl = Solution()

    print(sl.verifyPostorder([3, 10, 6, 9, 2]))
