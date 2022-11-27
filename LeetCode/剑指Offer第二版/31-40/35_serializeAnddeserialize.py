# 序列化二叉树
# 请实现两个函数，分别用来序列化和反序列化二叉树。
# 你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
import collections

from commonUtil import TreeNode, defineTestRoot


class Codec:

    def serialize(self, root: TreeNode):
        if not root:
            return []
        li = []
        queue = [root]
        nullNum = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if not cur:
                    li.append(None)
                else:
                    li.append(cur.val)
                if not cur:
                    nullNum += 2
                    queue.append(None)
                    queue.append(None)
                else:
                    if not cur.left:
                        nullNum += 1
                    if not cur.right:
                        nullNum += 1
                    queue.append(cur.left)
                    queue.append(cur.right)

            if len(queue) == nullNum:
                break
            nullNum = 0
        return li

    def deserialize(self, data: list):
        if len(data) == 0:
            return None
        head = TreeNode(data[0])
        cur = head
        data.insert(0, 0)
        for i in range(1, len(data)):
            if 2*i + 1 <= len(data)-1:
                cur.left = data[2 * i]
                cur.right = data[2 * i + 1]
        return head

    def serialize2(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize2(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == '__main__':
    cc = Codec()
    print(cc.serialize2(defineTestRoot()))
    print(cc.deserialize2(cc.serialize2(defineTestRoot())))
