# Definition for singly-linked list.
from commonUtil import prinNode, ListNode, defineTestListNode


# 链表中倒数第K个节点
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        q = head
        for i in range(k):
            q = q.next
        while q:
            p = p.next
            q = q.next

        return p


if __name__ == '__main__':
    head = defineTestListNode([1, 2, 3, 4])
    sl = Solution()
    prinNode(sl.getKthFromEnd(head, 2))
