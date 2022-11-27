
# 反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
from commonUtil import ListNode, defineTestListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        headnone = ListNode(0)
        headnone.next = head
        if head is None:
            return None
        p = head.next
        head.next = None
        while p:
            r = p.next
            p.next = headnone.next
            headnone.next = p
            p = r
        return headnone.next


def prinNode(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    sl = Solution()
    head = defineTestListNode([1, 2, 3, 4])
    prinNode(sl.reverseList(head))
