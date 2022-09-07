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
