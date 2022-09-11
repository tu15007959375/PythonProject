class Solution:
    def fib(self, n: int) -> int:
        return self.fibonacci(n) % 1000000007

    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        filist = [0] * (n + 1)
        filist[1] = 1
        for i in range(n - 1):
            filist[i + 2] = filist[i + 1] + filist[i]
        return filist[n]

    def fib2(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    sl = Solution()
    print(sl.fib(5))
