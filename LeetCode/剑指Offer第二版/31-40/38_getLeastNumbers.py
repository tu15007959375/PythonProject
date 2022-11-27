from typing import List


# 最小的K位数
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        res = []
        for _ in range(k):
            minnum = min(arr)
            res.append(minnum)
            arr.pop(arr.index(minnum))
        return res


if __name__ == '__main__':
    sl = Solution()
    print(sl.getLeastNumbers([3, 2, 1], 2))
