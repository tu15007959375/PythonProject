class CQueue(object):

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value):
        self.A.append(value)

    def deleteHead(self):
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A.pop:
            self.B.append(self.A.pop())
        return self.B.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
