class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> list:
    treequeue = [root]
    res = []
    while treequeue:
        for _ in range(len(treequeue)):

            treeNode = treequeue.pop(0)
            res.append(treeNode.val)
            if treeNode.left:
                treequeue.append(treeNode.left)
            if treeNode.right:
                treequeue.append(treeNode.right)
    return res
