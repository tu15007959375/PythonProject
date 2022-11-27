# 合并两个排序的链表
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
# 0124, 134
from commonUtil import ListNode, prinNode, defineTestListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        headone = ListNode(0)
        headone.next = l1
        prenode = headone
        while l1 and l2:
            if l1.val < l2.val:
                if l1.next is None:
                    l1.next = l2
                    break
                prenode = l1
                l1 = l1.next
            else:
                tmp = l2.next
                l2.next = l1
                prenode.next = l2
                prenode = l2
                l2 = tmp

        return headone.next


if __name__ == '__main__':
    sl = Solution()
    head1 = defineTestListNode([1, 2, 4])

    head2 = defineTestListNode([1, 3, 4])

    prinNode(sl.mergeTwoLists(head1, head2))
