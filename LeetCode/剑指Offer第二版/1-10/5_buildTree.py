# 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
from commonUtil import TreeNode


def buildTree(preorder, inorder):
    def recur(root, left, right):
        if left > right: return  # 递归终止
        node = TreeNode(preorder[root])  # 建立根节点
        i = dic[preorder[root]]  # 划分根节点、左子树、右子树
        node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
        node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
        return node  # 回溯返回根节点

    dic, preorder = {}, preorder
    for i in range(len(inorder)):
        dic[inorder[i]] = i
    return recur(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    node = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print('xxx')
