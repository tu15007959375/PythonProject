# Definition for singly-linked list.
# 删除链表的节点
# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。
from commonUtil import defineTestListNode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pnode = head
        while pnode.next:
            if pnode.next.val == val:
                pnode.next = pnode.next.next
                break
            pnode = pnode.next
        return head


def prinNode(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    head = defineTestListNode([0, -3, 5, 99])

    sl = Solution()
    prinNode(sl.deleteNode(head, -3))
