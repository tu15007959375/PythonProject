# 二叉搜索树和双向链表
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
from commonUtil import TreeNode, defineTestRoot


class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        def recur(Node: TreeNode):
            if not Node:
                return

            recur(Node.left)
            if self.pre:
                self.pre.right, Node.left = Node, self.pre
            else:
                self.head = Node
            self.pre = Node

            recur(Node.right)

        if not root:
            return
        self.pre = None
        recur(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

if __name__ == '__main__':
    sl = Solution()
    print(sl.treeToDoublyList(defineTestRoot()))
