import math
# 剪绳子1
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1]
# 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


class Solution:
    def cuttingRope(self, n: int) -> int:
        maxnum = 0
        if n == 1 or n == 2:
            return 1
        for i in range(2, n):
            x = int(n / i)
            y = int(n % i)
            maxnum = max(maxnum, pow(x, i - y) * pow(x + 1, y))
        return maxnum

    def cuttingRope2(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


if __name__ == '__main__':
    sl = Solution()
    print(sl.cuttingRope(2))
