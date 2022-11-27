# 字符串中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countdict = defaultdict(int)
        for li in nums:
            countdict[li] += 1
        countmax = max(countdict.values())
        for key, value in countdict.items():
            if value == countmax:
                return key


if __name__ == '__main__':
    sl = Solution()
    print(sl.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
