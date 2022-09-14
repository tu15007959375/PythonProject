# 从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reversePrint(head):
    return reversePrint(head.next) + [head.val] if head else []


if __name__ == '__main__':
    li = ListNode(2)
    li.next = ListNode(3)
    li.next.next = ListNode(1)
    print(reversePrint(li))
