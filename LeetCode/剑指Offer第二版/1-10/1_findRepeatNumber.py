# 数组中重复的数字
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

def findRepeatNumber(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]:
            return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == '__main__':
    inParam = [2, 3, 1, 0, 5, 5, 3]
    print(findRepeatNumber(inParam))
