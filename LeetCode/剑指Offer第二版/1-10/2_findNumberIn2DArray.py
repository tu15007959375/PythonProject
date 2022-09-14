# 二维数组中的查找
# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def findNumberIn2DArray(matrix, target):
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            return False
        if matrix[i][0] > target:
            continue
        for j in range(len(matrix[i])):
            if matrix[i][j] > target:
                continue
            if matrix[i][j] == target:
                return True
    return False


if __name__ == '__main__':
    inMatrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    inTarget = 0
    print(findNumberIn2DArray(inMatrix, inTarget))
