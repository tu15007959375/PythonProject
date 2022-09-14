# 二进制中1的个数
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
class Solution:
    def hammingWeight(self, n: int) -> int:
        countnum = 0
        if n == 0:
            return 0
        while n:
            if n % 2:
                countnum += 1
            n = int(n / 2)
        return countnum

    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
            # n &= n - 1
        return res


if __name__ == '__main__':
    sl = Solution()
    print(sl.hammingWeight(128))
