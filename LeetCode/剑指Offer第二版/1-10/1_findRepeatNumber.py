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
