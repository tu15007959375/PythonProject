from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def defineTestListNode(li: List[int]) -> ListNode:
    head = ListNode(li[0])
    p = head
    for i in range(1, len(li)):
        p.next = ListNode(li[i])
        p = p.next
    return head


def defineTestRoot() -> TreeNode:
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(9)
    return root


def prinNode(head: ListNode):
    while head:
        print(head.val)
        head = head.next


def printTree(root: TreeNode):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


def levelOrder(root: TreeNode) -> list:
    treequeue = [root]
    res = []
    while treequeue:
        treeNode = treequeue.pop(0)
        res.append(treeNode.val)
        if treeNode.left:
            treequeue.append(treeNode.left)
        if treeNode.right:
            treequeue.append(treeNode.right)

    return res

