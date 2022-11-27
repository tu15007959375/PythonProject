# 从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
from commonUtil import ListNode, defineTestListNode


def reversePrint(head):
    return reversePrint(head.next) + [head.val] if head else []


if __name__ == '__main__':
    li = defineTestListNode([2, 3, 1])
    print(reversePrint(li))
