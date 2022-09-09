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
