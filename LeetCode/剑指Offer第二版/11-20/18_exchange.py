from typing import List


# 调整数组顺序使奇数位于偶数前面
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                if nums[right] % 2 != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    right -= 1
            else:
                left += 1

        return nums


if __name__ == '__main__':
    sl = Solution()
    print(sl.exchange([1, 2, 3, 4]))
