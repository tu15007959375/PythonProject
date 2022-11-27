from typing import List


# 打印从1到最大的n位数
# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n == 0:
            return []
        number = pow(10, n) - 1
        arr = []
        for i in range(1, number + 1):
            arr.append(i)
        return arr
        # return list(range(1, 10 ** n))


if __name__ == '__main__':
    sl = Solution()
    print(sl.printNumbers(5))
